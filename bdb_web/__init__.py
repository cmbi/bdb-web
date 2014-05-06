import logging
import os

from flask import Flask
from flask_flatpages import FlatPages, pygments_style_defs
from flask_flatpages_pandoc import FlatPagesPandoc

from werkzeug.wsgi import DispatcherMiddleware



_log = logging.getLogger("bdb")
log_file = os.path.join("bdb-web.log")
_file = logging.FileHandler(log_file, "a")
_log.addHandler(_file)
_cons = logging.StreamHandler()
_log.addHandler(_cons)
_formatter1 = logging.Formatter(
        "%(asctime)s | %(levelname)-7s | %(message)s | "
        "[in %(pathname)s:%(lineno)d]")
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

application = DispatcherMiddleware(Flask('dummy_app'),
                                   {app.config['APPLICATION_ROOT']: app})

if not app.debug:
    from logging.handlers import SMTPHandler
    mail_handler = SMTPHandler((app.config["MAIL_SERVER"],
                                app.config["MAIL_SMTP_PORT"]),
                               app.config["MAIL_FROM"],
                               app.config["MAIL_TO"],
                               "bdb-web failed")
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)
    mail_handler.setFormatter(logging.Formatter("""
    Message type:       %(levelname)s
    Location:           %(pathname)s:%(lineno)d
    Module:             %(module)s
    Function:           %(funcName)s
    Time:               %(asctime)s

    Message:

    %(message)s
    """))

flat_pages = FlatPages(app)
FlatPagesPandoc("markdown", app, ["--mathml", ], pre_render=True)


import bdb_web.views
