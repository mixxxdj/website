# Server Installation

These instructions are based on Ubuntu 16.04.

## Packages to Install

Required:
* apache2
* libapache2-mod-php5.6
* mariadb-server
* memcached
* php-memcache (needed?)
* php-memcached
* php5.6-common
* php5.6-gd
* php5.6-json
* php5.6-mysql
* php5.6-xml (used by Dokuwiki)
* mailutils (postfix, etc.)
* google-cloud-sdk (for backups)
* unzip (for phpBB upgrades)

Optional (helpful for tuning / monitoring):
* apachetop
* atop
* htop
* mysqltuner
* mytop

Debian package sources (may be stale):
* http://ppa.launchpad.net/ondrej/php/ubuntu
* https://packages.cloud.google.com/apt

## Post-install Edits

### /etc/postfix/main.cf

Set:
* `myhostname = mixxx.org`
* `mydestination = localhost.org, , localhost`
* `inet_interfaces = loopback-only`

### /etc/memcached.conf

Set RAM usage (e.g. 32MB)
* `-m 32`

### phpBB HTTPS Mode

If you are reverse-proxying mixxx.org through something that terminates TLS
(e.g. CloudFlare, which we do as of 4/2017), then you need to inform phpBB that
it is running over HTTPS. Otherwise, plugins like reCAPTCHA will serve their
assets over HTTP, which will be blocked.

One way of doing this is to edit `forums/config.php` to include:

* `$_SERVER['HTTPS'] = 'on';`
* `$_SERVER['SERVER_PORT'] = 443;`

In the phpBB Administrator Control Panel, under Cookie Settings you may also
want to enable secure cookies. (It's unclear whether this is actually needed.)

# Backup

The website is always deployed from the latest state of the Git repository, so
the static content does not need backup. The wiki and forums need regular
backups. Our fabfile can automatically backup the wiki and forums and upload the
resulting snapshots to Google Cloud Storage. As long as you have SSH-access to
the server, run the following command:

  `fab production snapshot gcloud_upload`

# Wiki Upgrade

If you are logged in as an admin, available upgrades will be listed at the top
of every page. To upgrade:

* Backup the site (see "Backups" above).
* Go to
  [Wiki Upgrade](https://mixxx.org/wiki/doku.php/start?do=admin&page=upgrade)
  from the admin page.
* Go through the easy step-by-step process. All permissions should be setup so
  that an admin can do this without SSH access.

# Forum Upgrade

**WARNING: We are currently on the 3.0.x release. Do not upgrade to 3.1.x with
these instructions. That process is much more involved.**

* Backup the site (see "Backups" above).
* Download the latest "autoupdate" package from
  [phpBB](https://www.phpbb.com/downloads/#update). Note that we are currently
  on the 3.0.x cycle. Do not download an auto-upgrade package for 3.1.x.
* Unzip the archive into /home/mixxx/public_html/forums/
  * Replace all `doc/` files if asked.
  * Verify `install/` folder is now present.
  * **The forums are now down (users will see an error page).**
* Navigate to https://mixxx.org/forums/install
* Follow step by step instructions.
* If unmergeable diffs are identified, view the diffs and verify they are ok.
* Confirm your choices and download an update archive.
* Transfer the update archive to /home/mixxx/public_html/forums/ and unarchive it (overwrite all existing files).
* Move `install` and `upgrade_3.0.x_to_3.0.y.tar.gz` to `junkyard/` (for posterity).
  * **The forums are now back up.**
* Log in and verify everything works.
