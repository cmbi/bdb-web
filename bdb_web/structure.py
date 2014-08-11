import logging
_log = logging.getLogger("bdb-web")

import Bio.PDB


from bdb_web import bdb_data


def get_b_factors(structure, first_model_only=True, ca=False, norm=False):
    """Get the B-factor values of this Bio.PDB.Structure.

    Return a list with for each chain a list of tuples.
    A tuple contains the full id of the atom and its B-factor.
    Also return the total number of B-factors in the nested list

    first_model_only returns only the first model (if there are multiple)
        this prevents overflow errors if a figure has to be created on a
        matplotlib canvas..

    Return B-factors for Calpha atoms only if ca is true.

    Return normalized B-factors if norm=True.
    Normalization now is simply (x - mean(all B))/sd(all B) and is performed
        separately for each chain

    Return an empty list if the structure does not have atoms.
    """
    c_list = []
    b_num = 0

    for chain in structure[0]:
        b_list = []
        for atom in chain.get_atoms():
            b_list.append((atom.get_full_id(), atom.get_bfactor()))
            b_num = b_num + 1
        c_list.append(b_list)
    return c_list, b_num


def create_structure(_id, xyz, verbose=False):
    """Create a Bio.PDB.Structure for the given xyz coordinate file.

    Return None if a Structure could not be created.
    """
    structure = None

    try:
        p = Bio.PDB.PDBParser(QUIET=not verbose)
        structure = p.get_structure(_id, xyz)
    except IOError as ie:
        _log.error(ie)
    except (AttributeError, IndexError, ValueError, AssertionError,
            Bio.PDB.PDBExceptions.PDBConstructionException) as be:
        # (temporary fix until Biopython parser is fixed)
        _log.error("Biopython Error. {}".format(be))

    return structure


def get_structure(_id, db="pdb", verbose=False):
    """Return a Bio.PDB.Structure for the given xyz coordinate file.

    Return None if a Structure could not be created.
    Raise an exception if creation goes wrong.
    """
    structure = None

    if db == "pdb":
        xyz = bdb_data.pdb_path(_id)
    elif db == "bdb":
        xyz = bdb_data.bdb_path(_id)
    _log.info("Loading {}...".format(xyz))

    structure = create_structure(_id, xyz)
    return structure
