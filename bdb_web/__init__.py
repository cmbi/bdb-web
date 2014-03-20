from flask import Flask
import logging
import os

_log = logging.getLogger("bdb")
log_file = os.path.join("bdb-web.log")
_file = logging.FileHandler(log_file, "a")
_log.addHandler(_file)
_cons = logging.StreamHandler()
_log.addHandler(_cons)
_formatter1 = logging.Formatter(
        "%(asctime)s | %(levelname)-7s | %(message)s")
_formatter2 = logging.Formatter(
        "%(message)s")
_log.setLevel(logging.INFO)
_file.setFormatter(_formatter1)
_cons.setFormatter(_formatter2)

app = Flask(__name__)
app.config.from_envvar("BDB_WEB_SETTINGS")

import bdb_web.views
