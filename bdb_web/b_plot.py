import logging
_log = logging.getLogger("bdb-web")


import StringIO

from flask import make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

from bdb_web.structure import get_b_factors, get_structure


def show(pdb_id, ca=True):
    """Create B-factor plots for both BDB and PDB entries.

    If ca is false, show a bigger plot with all atoms

    If the pdb_id is invalid return None.
    If both PDB and BDB entries do not exist, return None.
    If only the BDB entry does not exist, only plot the PDB B-factors.
    """
    response = None
    less_ticks = False

    # Create Bio.PDB structures
    sp = get_structure(pdb_id, "pdb")
    if not sp:
        return None
    sb = get_structure(pdb_id, "bdb")

    # PDB
    # Get a list of (full atom id, B-factor) tuples
    bp = get_b_factors(sp)

    # Create the figure
    fig_size = (23, 12)
    if not ca:
        fig_size = (len(bp)*0.2, 12)
        if fig_size[0] > 2417:
            _log.debug("Figure width ({}) too large. Setting max width".
                       format(fig_size[0]))
            fig_size = (409, 12)
            less_ticks = True
    fig = Figure(figsize=fig_size)
    ax = fig.add_subplot(111)
    ax.plot([b[1] for b in bp], color='grey', ls='-', lw=2)
    ax.set_title(pdb_id)
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
    # TODO select ONLY CALPHA
    xt = np.arange(0, len(bp), 5*int(len(bp)/100))
    # major x-tick labels with residue id
    xtl = [''.join((lb[0][2], ''.join(str(l) for l in lb[0][3]))) for lb in bp]
    # minor x-tick position
    xtm = np.arange(0, len(bp), int(len(bp)/100))
    if not ca:
        xt = np.arange(0, len(bp))
        # also add atom id
        xtl = [''.join(
            (lb[0][2], ''.join(str(l) for l in lb[0][3]),
             ''.join(str(m) for m in lb[0][4]))) for lb in bp]
    if less_ticks:
        xt = np.arange(0, len(bp), 2*int(len(bp)/500))
        xtl = [''.join(
            (lb[0][2], ''.join(str(l) for l in lb[0][3]),
             ''.join(str(m) for m in lb[0][4]))) for lb in bp]
        xtm = np.arange(0, len(bp), int(len(bp)/500))
    xtl = np.take(xtl, xt)

    # Set vertical ticks
    ax.xaxis.set_ticks(xt)
    ax.xaxis.set_ticklabels(xtl)
    if ca or less_ticks:
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
