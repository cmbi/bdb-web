from flask import Flask
from flask_flatpages import FlatPages, pygments_style_defs
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

FLATPAGES_EXTENSION = ".md"
FLATPAGES_MARKDOWN_EXTENSIONS = ["codehilite", "tables", "def_list",
                                 "footnotes", "admonition", "fenced_code"]

app = Flask(__name__, static_folder="static")
app.config.from_object(__name__)
app.config.from_envvar("BDB_WEB_SETTINGS")
flat_pages = FlatPages(app)

import bdb_web.views
