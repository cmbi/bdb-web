import logging
from logging.handlers import RotatingFileHandler, SMTPHandler

_log = logging.getLogger("bdb-web")
log_file = "bdb-web.log"
_file = RotatingFileHandler(log_file, "a", 524288, 5, "UTF-8")
_log.addHandler(_file)
_formatter = logging.Formatter(
    "%(asctime)s | %(levelname)-7s | %(message)s "
    "[in %(pathname)s:%(lineno)d]")
_log.setLevel(logging.INFO)
_file.setFormatter(_formatter)


from flask import Flask
from flask_flatpages import FlatPages
from flask_flatpages_pandoc import FlatPagesPandoc


FLATPAGES_EXTENSION = ".md"
FLATPAGES_MARKDOWN_EXTENSIONS = ["codehilite", "tables", "def_list",
                                 "footnotes", "admonition", "fenced_code"]
MATHJAX_CDN = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
MATHJAX_ARG = "--mathjax={:s}".format(MATHJAX_CDN)

app = Flask(__name__, static_folder="static")
app.config.from_object(__name__)
app.config.from_envvar("BDB_WEB_SETTINGS")

from bdb_web.rev_proxy import ReverseProxied
app.wsgi_app = ReverseProxied(app.wsgi_app)

if not app.debug:
    app.logger.addHandler(_file)
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
else:
    _log.setLevel(logging.DEBUG)

flat_pages = FlatPages(app)
from bdb_web.renderer import renderer
FlatPagesPandoc.renderer = renderer
FlatPagesPandoc("markdown", app, [MATHJAX_ARG, "-s", "--quiet"],
                pre_render=True)


import bdb_web.views
if app.debug:
    bdb_web.views.we_are_running()
