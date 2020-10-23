import datetime
import os

from fabric.api import *
import fabric.contrib.project as project
from fabric.contrib.files import exists

LANGUAGE_CONFIGS = {
    "en": {"dest_path": "/"},
    "de": {"dest_path": "/de"},
    "de-DE": {"dest_path": "/de-DE"},
}

env.use_ssh_config = True
env.roledefs = {
    "production": {
        "hosts": ["direct.mixxx.org"],
        "dest_path": "/home/mixxx/public_html",
    },
    "staging": {
        "hosts": ["direct.mixxx.org"],
        "dest_path": "/home/mixxx/domains/staging.mixxx.org/public_html",
    },
}

env.deploy_path = ".build"
DEPLOY_PATH = env.deploy_path
env.user = "mixxx"
BACKUP_GS_BUCKET = "gs://mixxxdj-website-backup/snapshots/"
BACKUP_USER = "mixxx"
BACKUP_PATH = "/home/{}/backups".format(BACKUP_USER)
FORUMS_DATABASE_NAME = "phpbb"
FORUMS_DATABASE_USER = "phpbb"
FORUMS_DATABASE_PASSWORD = ""  # Do not commit the password.


def staging():
    env.instance_name = "staging"
    env.roles = ["staging"]
    env.dest_path = env.roledefs["staging"]["dest_path"]


def production():
    env.instance_name = "production"
    env.roles = ["production"]
    env.dest_path = env.roledefs["production"]["dest_path"]


def clean():
    if os.path.isdir(DEPLOY_PATH):
        local("rm -rf {deploy_path}".format(**env))
        local("mkdir {deploy_path}".format(**env))


def build(language="en"):
    config = LANGUAGE_CONFIGS.get(language, None)
    if config is None:
        raise Exception("Invalid language: %s" % language)
    config_file = (
        "config.%s.json" % language if language != "en" else "config.json"
    )
    local("cactus build -c %s" % config_file)
    if "dest_path" in env:
        env.dest_path = env.dest_path + config["dest_path"]


def rebuild(*args, **kwargs):
    clean()
    build(*args, **kwargs)


def serve(language="en"):
    clean()
    config = LANGUAGE_CONFIGS.get(language, None)
    if config is None:
        raise Exception("Invalid language: %s" % language)
    config_file = (
        "config.%s.json" % language if language != "en" else "config.json"
    )
    local("cactus serve -c %s" % config_file)


def publish():
    project.rsync_project(
        remote_dir=env.dest_path,
        local_dir=DEPLOY_PATH.rstrip("/") + "/",
        exclude=(".DS_Store", ".git"),
        delete=False,
        extra_opts="-c",
    )


def snapshot_path(instance_name, snapshot_name):
    return os.path.join(BACKUP_PATH, instance_name, "snapshots", snapshot_name)


def gcloud_snapshot_path(instance_name, snapshot_name):
    return os.path.join(BACKUP_GS_BUCKET, instance_name, snapshot_name)


def snapshot(snapshot_name=None):
    instance_path = env.dest_path
    assert FORUMS_DATABASE_PASSWORD, "FORUMS_DATABASE_PASSWORD is empty."

    if snapshot_name is None:
        snapshot_name = datetime.datetime.now().strftime("%Y-%m-%d")
    snap_path = snapshot_path(env.instance_name, snapshot_name)

    assert snap_path

    if exists(snap_path):
        raise Exception(
            "WARNING: Snapshot '{}' already exists at '{}'.".format(
                snapshot_name, snap_path
            )
        )

    sudo("mkdir -p {}".format(snap_path), user=BACKUP_USER)
    with cd(snap_path), settings(sudo_user=BACKUP_USER):
        forums_path = os.path.join(instance_path, "forums")
        forums_snapshot = "forums.tar.gz"
        sudo("tar czf {} -C {} .".format(forums_snapshot, forums_path))

        mysql_snapshot = "forums.sql.gz"
        sudo(
            "mysqldump -u{} -p{} {} | gzip > {}".format(
                FORUMS_DATABASE_USER,
                FORUMS_DATABASE_PASSWORD,
                FORUMS_DATABASE_NAME,
                mysql_snapshot,
            )
        )

        wiki_path = os.path.join(instance_path, "wiki")
        wiki_snapshot = "wiki.tar.bz2"
        # Exclusions to save space & time per https://www.dokuwiki.org/faq:backup
        sudo(
            "tar --exclude='data/cache' --exclude='data/index' --exclude='data/locks' --exclude='data/tmp' -cjpf {} -C {} .".format(
                wiki_snapshot, wiki_path
            )
        )

    # Record snapshot name for chaining commands.
    env.snapshot_name = snapshot_name


def gcloud_upload(snapshot_name=None):
    instance_path = env.dest_path
    if snapshot_name is None:
        # If we ran snapshot then we recorded the snapshot name in env.
        if hasattr(env, "snapshot_name"):
            snapshot_name = env.snapshot_name
        else:
            snapshot_name = datetime.datetime.now().strftime("%Y-%m-%d")
    snap_path = snapshot_path(env.instance_name, snapshot_name)
    assert snap_path
    if not exists(snap_path):
        raise Exception(
            "WARNING: Snapshot '{}' does not exist at '{}'.".format(
                snapshot_name, snap_path
            )
        )

    gcloud_path = gcloud_snapshot_path(env.instance_name, snapshot_name)
    run("gsutil -m rsync -d -r {} {}".format(snap_path, gcloud_path))
