import logging
_log = logging.getLogger("bdb-web")

import Bio.PDB


from bdb_web import bdb_data


def get_b_factors(structure):
    """Return the B-factors of this Bio.PDB.Structure as a list of tuples.

    The tuple contains the full id of the atom and its B-factor.
    Return an empty list if the structure does not have atoms.
    """
    b_list = []

    for atom in structure.get_atoms():
        b_list.append((atom.get_full_id(), atom.get_bfactor()))

    return b_list


def create_structure(_id, xyz, verbose=False):
    """Create a Bio.PDB.Structure for the given xyz coordinate file.

    Return None if a Structure could not be created.
    Raise an exception if creation goes wrong.
    """
    structure = None

    try:
        p = Bio.PDB.PDBParser(QUIET=not verbose)
        structure = p.get_structure(_id, xyz)
    except (AttributeError, IndexError, ValueError, AssertionError,
            Bio.PDB.PDBExceptions.PDBConstructionException) as e:
        # (temporary fix until Biopython parser is fixed)
        _log.error('Biopython Error. {}'.format(e))

    return structure


def get_structure(_id, db='pdb', verbose=False):
    """Return a Bio.PDB.Structure for the given xyz coordinate file.

    Return None if a Structure could not be created.
    Raise an exception if creation goes wrong.
    """
    structure = None

    if db == 'pdb':
        xyz = bdb_data.pdb_path(_id)
    elif db == 'bdb':
        xyz = bdb_data.bdb_path(_id)
    _log.info('Loading {}...'.format(xyz))

    structure = create_structure(_id, xyz)
    return structure
