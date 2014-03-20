from flask import render_template, send_from_directory

from bdb_web import app

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
            )

@app.route("/404")
def error():
    pass

if __name__ == '__main__':
    app.run()
