from flask import render_template, send_from_directory
from flask_flatpages import pygments_style_defs

from bdb_web import app, flat_pages

import bdb_data

import logging
_log = logging.getLogger("bdb")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/bdb/<pdb_id>")
def bdb(pdb_id=None):
    if pdb_id is None:
        # TODO: Send json response to web page so it can display an error.
        pass
    else:
        return render_template(
                "bdb.html",
                bdb_metadata=bdb_data.parse_bdb_metadata(pdb_id),
                bdb_url=bdb_data.generate_bdb_url(pdb_id),
                whynot_url=bdb_data.generate_whynot_url(pdb_id)
                )

@app.route("/download/<pdb_id>")
def download(pdb_id):
    return send_from_directory(
            directory=bdb_data.bdb_dir(pdb_id),
            filename=pdb_id + ".bdb",
            mimetype="chemical/x-pdb",
            as_attachment=True,
            attachment_filename=pdb_id + ".bdb"
            )

@app.route("/<name>/")
def pages(name):
    page = flat_pages.get_or_404(name)
    return render_template("page.html", page=page)

@app.route("/pygments.css")
def pygments_css():
    return (pygments_style_defs("solarizedlight"), 200,
            {"Content-Type": "text/css"})

@app.errorhandler("404")
def page_not_found(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run()
