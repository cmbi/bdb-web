import logging
_log = logging.getLogger("bdb-web")


import datetime
import StringIO
import random


from flask import make_response

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter


from bdb_web.structure import get_b_factors, get_structure


def show(pdb_id):
    sp = get_structure(pdb_id, "pdb")
    sb = get_structure(pdb_id, "bdb")

    bp = get_b_factors(sp)
    bb = get_b_factors(sb)

    fig = Figure(figsize=(23, 12))
    ax = fig.add_subplot(111)
    ax.plot([b[1] for b in bp], color='grey', ls='-', lw=2)
    ax.plot([b[1] for b in bb], color='black', ls='-', lw=2)
    ax.set_ylabel('B-factor')
    ax.legend(('pdb', 'bdb'))

    xt = [''.join((lb[0][2], ''.join(str(l) for l in lb[0][3]))) for lb in bp]
    ax.set_xticks(range(len(bp)), xt)

    canvas = FigureCanvas(fig)
    output = StringIO.StringIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = "image/png"
    return response
