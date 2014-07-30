import logging
_log = logging.getLogger("bdb-web")


import StringIO

from flask import make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

from bdb_web.structure import get_b_factors, get_structure


def show(pdb_id):
    """Create B-factor plots for both BDB and PDB entries.

    If the pdb_id is invalid return None.
    If both PDB and BDB entries do not exist, return None.
    If only the BDB entry does not exist, only plot the PDB B-factors.
    """
    response = None

    # Create Bio.PDB structures
    sp = get_structure(pdb_id, "pdb")
    if not sp:
        return None
    sb = get_structure(pdb_id, "bdb")

    # PDB
    # Get a list of (full atom id, B-factor) tuples
    bp = get_b_factors(sp)

    # Create the figure
    fig = Figure(figsize=(23, 12))
    ax = fig.add_subplot(111)
    ax.plot([b[1] for b in bp], color='grey', ls='-', lw=2)
    ax.set_ylabel('B-factor')

    # BDB
    if sb:
        bb = get_b_factors(sb)
        ax.plot([b[1] for b in bb], color='black', ls='-', lw=2)
        ax.legend(('pdb', 'bdb'))
    else:
        ax.legend('pdb')

    # Full atom id as x-ticks
    # major x-tick position
    xt = np.arange(0, len(bp), 5*int(len(bp)/100))
    # major x-tick labels
    xtl = [''.join((lb[0][2], ''.join(str(l) for l in lb[0][3]))) for lb in bp]
    xtl = np.take(xtl, xt)
    # major x-tick position
    xtm = np.arange(0, len(bp), int(len(bp)/100))


    # Set vertical ticks
    ax.xaxis.set_ticks(xt)
    ax.xaxis.set_ticklabels(xtl)
    ax.xaxis.set_ticks(xtm, minor=True)
    for label in ax.xaxis.get_ticklabels():
        label.set_rotation('vertical')

    # Create a response
    canvas = FigureCanvas(fig)
    output = StringIO.StringIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = "image/png"

    return response
