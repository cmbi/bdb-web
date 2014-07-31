import logging
_log = logging.getLogger("bdb-web")


from flask import (g, redirect, request, render_template,
                   send_from_directory, url_for)
from flask_flatpages import pygments_style_defs


from bdb_web import app, bdb_data, b_plot, flat_pages, forms


@app.route("/entry/<pdb_id>/")
def bdb(pdb_id):
    pdb_id = pdb_id.lower()
    return render_template(
        "bdb.html",
        bdb_metadata=bdb_data.parse_bdb_metadata(pdb_id),
        bdb_url=bdb_data.generate_bdb_url(pdb_id),
        pdb_url=bdb_data.generate_pdb_url(pdb_id),
        tlsanl_log_url=bdb_data.generate_tlsanl_log_url(pdb_id),
        whynot_url=bdb_data.generate_whynot_url(pdb_id))


@app.route("/bplot_ca/<pdb_id>.png")
def bplot_ca(pdb_id):
    pdb_id = pdb_id.lower()
    fig = b_plot.show(pdb_id, ca=True)
    if not fig:
        return page_not_found(
            ValueError('Could not create C-alpha B-factor plot for {}'.format(
                pdb_id)))
    return fig


@app.route("/bplot_ca_norm/<pdb_id>.png")
def bplot_ca_norm(pdb_id):
    pdb_id = pdb_id.lower()
    fig = b_plot.show(pdb_id, ca=True, norm=True)
    if not fig:
        return page_not_found(
            ValueError('Could not create normalized C-alpha'
                       'B-factor plot for {}'.format(pdb_id)))
    return fig


@app.route("/bplot/<pdb_id>.png")
def bplot(pdb_id):
    pdb_id = pdb_id.lower()
    fig = b_plot.show(pdb_id, ca=False)
    if not fig:
        return page_not_found(
            ValueError('Could not create B-factor plot for {}'.format(pdb_id)))
    return fig


@app.route("/download/<pdb_id>/")
def download(pdb_id):
    pdb_id = pdb_id.lower()
    return send_from_directory(
        directory=bdb_data.bdb_dir(pdb_id),
        filename=pdb_id + ".bdb",
        mimetype="chemical/x-pdb",
        as_attachment=True,
        attachment_filename=pdb_id + ".bdb")


@app.route("/")
def index():
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html"), 500


@app.route("/<name>/")
def pages(name):
    page = flat_pages.get_or_404(name)
    return render_template("page.html", page=page)


@app.route("/pygments.css")
def pygments_css():
    return (pygments_style_defs("solarizedlight"), 200,
            {"Content-Type": "text/css"})


@app.route("/search/")
def search():
    form = forms.SearchForm(request.args)
    if not form.validate():
        return (render_template("search.html", form=form))
    return redirect(url_for("bdb", pdb_id=form.name.data))


@app.route("/tlsanl_log/<pdb_id>/")
def tlsanl_log(pdb_id):
    pdb_id = pdb_id.lower()
    return send_from_directory(
        directory=bdb_data.bdb_dir(pdb_id),
        filename="tlsanl.log",
        mimetype="text/plain",
        as_attachment=False)


@app.before_request
def before_request():
    g.search_form = forms.SearchForm(request.args)


def we_are_running():
    _log.debug("BDB-web running!")
