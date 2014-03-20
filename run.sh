#!/usr/bin/env bash
export BDB_WEB_SETTINGS=~/projects/bdb-web/bdb_web_settings.cfg
gunicorn -k gevent -b localhost:5000 --debug bdb_web:app
