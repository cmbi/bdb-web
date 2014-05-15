#!/usr/bin/env bash
export BDB_WEB_SETTINGS=~/projects/bdb-web/config/bdb_web_settings.cfg
gunicorn -k gevent -b 0.0.0.0:5000 --debug bdb_web:app
