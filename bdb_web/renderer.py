from subprocess import Popen, PIPE

from flask import render_template_string, Markup

from bdb_web import _log


def renderer(self, text):
    """
    Renders a flat page to HTML.

    :param text: the text of the flat page
    :type text: string
    """

    # Fixes Flask-FlatPages-Pandoc version.
    if type(text) != str:
        text = str(text, self.app.config["FLATPAGES_ENCODING"])

    if self.pre_render:
        text = render_template_string(Markup(text))

    args = ["pandoc", "-f", self.source_format, "-t", "html"]
    args.extend(self.pandoc_args)

    _log.debug("Executing: %s", " ".join(args))

    proc = Popen(args, stdout=PIPE, stdin=PIPE, stderr=PIPE)
    html, stderr = proc.communicate(text.encode("utf8"))

    if stderr:
        raise ValueError(stderr)

    return html.decode("utf-8")
