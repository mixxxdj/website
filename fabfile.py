import os

from fabric.api import *
import fabric.contrib.project as project

LANGUAGE_CONFIGS = {
    'en': { 'dest_path': '/' },
    'de': { 'dest_path': '/de' },
    'de-DE': { 'dest_path': '/de-DE' }
}

env.use_ssh_config = True
env.roledefs = {
    'production': {
        'hosts': ['direct.mixxx.org'],
        'dest_path': '/home/mixxx/public_html',
    },
    'staging': {
        'hosts': ['direct.mixxx.org'],
        'dest_path': '/home/mixxx/domains/staging.mixxx.org/public_html',
    }
}

env.deploy_path = '.build'
DEPLOY_PATH = env.deploy_path
env.user = 'mixxx'

def staging():
    env.roles = ['staging']
    env.dest_path = env.roledefs['staging']['dest_path']

def production():
    env.roles = ['production']
    env.dest_path = env.roledefs['production']['dest_path']

def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build(language='en'):
    config = LANGUAGE_CONFIGS.get(language, None)
    if config is None:
        raise Exception('Invalid language: %s' % language)
    config_file = 'config.%s.json' % language if language != 'en' else 'config.json'
    local('cactus build -c %s' % config_file)
    if 'dest_path' in env:
        env.dest_path = env.dest_path + config['dest_path']

def rebuild(*args, **kwargs):
    clean()
    build(*args, **kwargs)

def serve(language='en'):
    clean()
    config = LANGUAGE_CONFIGS.get(language, None)
    if config is None:
        raise Exception('Invalid language: %s' % language)
    config_file = 'config.%s.json' % language if language != 'en' else 'config.json'
    local('cactus serve -c %s' % config_file)

def publish():
    project.rsync_project(
        remote_dir=env.dest_path,
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        exclude=('.DS_Store', '.git'),
        delete=False,
        extra_opts='-c',
    )
