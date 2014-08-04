from __future__ import division

import logging
_log = logging.getLogger("bdb-web")

import StringIO

from flask import make_response

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import numpy as np


from bdb_web.structure import get_b_factors, get_structure


def calc_fig_size(b_num, ca=True):
    """Calculate figure size.

    If Calpha, return standard figure size, otherwise take number of B-factors
    into account.

    Figure size is a (width, height) tuple
    Also return boolean indicating that downscaling is necessary
    """
    fig_size = (23, 12)
    downscale = False

    if not ca:
        fig_size = (b_num*0.2, 12)
        if fig_size[0] > 2417:
            _log.debug("Figure width ({}) too large. Setting max width".
                       format(fig_size[0]))
            fig_size = (409, 12)
            downscale = True

    return fig_size, downscale


def show(pdb_id, ca=True, norm=False):
    """Create B-factor plots for both BDB and PDB entries.

    If ca is false, show a bigger plot with all atoms
    If norm is true, subtract mean and scale to unit variance

    If the pdb_id is invalid return None.
    If both PDB and BDB entries do not exist, return None.
    If only the BDB entry does not exist, only plot the PDB B-factors.
    """
    response = None
    minor = ca

    # Create Bio.PDB structures
    sp = get_structure(pdb_id, "pdb")
    if not sp:
        return None
    sb = get_structure(pdb_id, "bdb")

    # PDB
    # Get a list of (full atom id, B-factor) tuples per chain
    bp, b_num = get_b_factors(sp)

    # Calculate figure size
    fig_size, minor = calc_fig_size(b_num=b_num, ca=ca)

    # Create the figure
    _log.debug("Creating figure...")
    fig = Figure(figsize=fig_size)
    ax = fig.add_subplot(111)

    # Set title, ylabel and grid
    ax.set_title(pdb_id)
    ylab = 'Normalized B-factor' if norm else 'B-factor'
    ax.set_ylabel(ylab)
    ax.grid(True)
    ax.set_axisbelow(True)

    # PDB B-factors
    b_fac_p, b_ind_p = get_bdata(chain_list=bp, ca=ca, norm=norm)
    b_fac_plot = [item for sublist in b_fac_p for item in sublist]
    p_line, = ax.plot(b_fac_plot, color='#B98C6A', ls='-', lw=2)

    # BDB B-factors
    if sb:
        bb, b_num = get_b_factors(sb)
        b_fac_b, b_ind_b = get_bdata(chain_list=bb, ca=ca, norm=norm)
        b_fac_blot = [item for sublist in b_fac_b for item in sublist]
        b_line, = ax.plot(b_fac_blot, color='#49597C', ls='-', lw=2)
        ax.legend(('pdb', 'bdb'))
    else:
        ax.legend('pdb')

    # Collapse the labels and indices
    # sub_bp = [bp[i] for i in b_ind_p]
    sub_bp = []
    for i, chain in enumerate(bp):
        for j in b_ind_p[i]:
            sub_bp.append(chain[j])

    # X-axis ticks and labels
    xt, xtl, xtm = get_xticks(b_list=sub_bp, ca=ca, minor=minor)
    ax.xaxis.set_ticks(xt)
    ax.xaxis.set_ticklabels(xtl, rotation='vertical')
    if len(xtm) > 0:
        ax.xaxis.set_ticks(xtm, minor=True)

    # Create a response
    canvas = FigureCanvas(fig)
    output = StringIO.StringIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = "image/png"

    _log.debug("'Uploading' figure...")

    return response


def get_bdata(chain_list, ca=False, norm=False):
    """Return B-factor values to plot and selected indices from b_list.
    Both lists are numpy arrays.

    Return B-factors for Calpha atoms only if ca is true.
    Return normalized B-factors if norm=True.
    The indices are also chain-specific

    Normalization now is simply (x - mean(all B))/sd(all B) and is performed
    chain-wise for the B-factors in chain_list.
    """
    b_inds = []
    b_vals = []

    # Keep track of position in structure
    # pos = 0
    for chain in chain_list:
        # Get the values and indices for each chain
        val, ind = get_bdata_chain(b_list=chain, ca=ca, norm=norm)

        # Shift the indices
        # ind = ind + pos
        b_inds.append(ind)
        # pos = pos + len(chain)

        # Values
        b_vals.append(val)

    return b_vals, b_inds


def get_bdata_chain(b_list, ca=False, norm=False):
    """Return B-factor values to plot and selected indices from b_list.
    Both lists are numpy arrays.

    Return B-factors for Calpha atoms only if ca is true.
    Return normalized B-factors if norm=True.

    Normalization now is simply (x - mean(all B))/sd(all B) and is performed for
    all B-factors in b_list.
    """
    b_inds = []
    if ca:
        b_inds = [i for i, b in enumerate(b_list) if b[0][4][0] == 'CA']
    else:
        b_inds = np.arange(0, len(b_list))

    b_vals = [b[1] for b in b_list]
    b_vals = np.take(b_vals, b_inds)

    if norm:
        mean = np.mean(b_vals)
        sd = np.std(b_vals)
        b_vals = [(b - mean)/sd for b in b_vals]

    return b_vals, np.array(b_inds)


def get_xticks(b_list, ca=False, minor=False):
    """Create major ticks and labels and minor tick locations for X-axis.

    Full atom ids are used to create tick labels

    If minor is true, return fewer major and minor ticks
    If minor is false, return only major ticks at every atom position in b_list
    """
    maj_loc = []
    maj_lab = []
    min_loc = []

    max_ticks = 138
    bl = len(b_list)

    # Full atom id as x-tick labels
    maj_lab = [''.join((lb[0][2], ''.join(str(l) for l in lb[0][3]),
               ''.join(str(m) for m in lb[0][4]))) for lb in b_list]

    # Default major ticks: all atoms
    maj_loc = np.arange(0, bl)
    if ca:
        # scale to max_ticks
        scale = bl/max_ticks
        if scale > 1.0:
            min_loc = np.unique(np.rint(np.arange(0, bl, scale)))
            min_loc = min_loc.astype(int)
            maj_loc = min_loc[0::2]

    elif minor:
        scale = int(bl/1000)
        maj_loc = np.arange(0, bl, 2*scale if scale > 0 else 1)
        min_loc = np.arange(0, bl, scale if scale > 0 else 1)

    maj_lab = np.take(maj_lab, maj_loc)
    _log.debug("Plotting {} xlabs".format(len(maj_lab)))

    return maj_loc, maj_lab, min_loc
