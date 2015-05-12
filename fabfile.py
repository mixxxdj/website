import os

from fabric.api import *
from fabric.state import env
import fabric.contrib.project as project

STAGING_HOST = 'stacktrace.org'
STAGING_DEST_PATH = '/home/mixxx/domains/staging.mixxx.org/public_html'
PROD_HOST = 'stacktrace.org'
PROD_DEST_PATH = '/home/mixxx/public_html'

env.deploy_path = '.build'
DEPLOY_PATH = env.deploy_path

env.user = 'mixxx'

def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    local('cactus build')

def rebuild():
    clean()
    build()

def serve():
    clean()
    local('cactus serve')

@hosts(PROD_HOST)
def publish():
    project.rsync_project(
        remote_dir=PROD_DEST_PATH,
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        exclude=('.DS_Store', '.git'),
        delete=False,
        extra_opts='-c',
    )

@hosts(STAGING_HOST)
def staging():
    project.rsync_project(
        remote_dir=STAGING_DEST_PATH,
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        exclude=('.DS_Store', '.git'),
        delete=False,
        extra_opts='-c',
    )
