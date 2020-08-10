#!/usr/bin/env bash
export BDB_WEB_SETTINGS=~/projects/bdb-web/config/bdb_web_settings.cfg
gunicorn -b 0.0.0.0:5000 --reload --log-level debug bdb_web:app
