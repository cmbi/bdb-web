from flask import url_for
from bdb_web import app
import json
import os
import re

import logging
_log = logging.getLogger("bdb")

PDB_ID_PAT = re.compile(r"^[0-9a-zA-Z]{4}$")

def bdb_dir(pdb_id, bdb_root=app.config["BDB_ROOT"]):
    """Return the BDB directory for this pdb_id.

    pdb_id validation is performed by valid_pdb_id
    """
    pdb_id = valid_pdb_id(pdb_id)
    return os.path.join(bdb_root, pdb_id[1:3], pdb_id)

def bdb_exists(pdb_id):
    """Return True if this BDB file exists.

    pdb_id validation is performed by valid_pdb_id
    """
    return os.path.isfile(bdb_path(pdb_id.lower()))

def bdb_path(pdb_id):
    """Return the path to this BDB file.

    pdb_id validation is performed by valid_pdb_id
    """
    pdb_id = valid_pdb_id(pdb_id)
    return os.path.join(bdb_dir(pdb_id), pdb_id + ".bdb")

def generate_bdb_url(pdb_id):
    """Return a url for downloading the BDB file if it exists, else None.

    pdb_id validation is performed by valid_pdb_id
    """
    bdb_url = None
    if bdb_exists(pdb_id):
        bdb_url = url_for("download", pdb_id=pdb_id)
    return bdb_url

def generate_whynot_url(pdb_id):
    """Return a url to the WHY NOT file for this pdb_id.

    Return None if this WHY NOT file does not exist

    pdb_id validation is performed by valid_pdb_id
    """
    whynot_url = None
    pdb_id = valid_pdb_id(pdb_id)
    if whynot_exists(pdb_id):
        try:
            whynot_url = app.config["WHY_NOT_SEARCH_URL"] + str(pdb_id)
        except TypeError:
            raise ValueError("PDB identifier should be a string")
    return whynot_url

def parse_bdb_metadata(pdb_id):
    """Parse BDB file metadata in json format.

    pdb_id validation is performed by valid_pdb_id
    """
    metadata = None
    json_name = os.path.join(bdb_dir(pdb_id), pdb_id + ".json")
    try:
        with open(json_name, "r") as jf:
            metadata = json.load(jf)
            metadata = prepare_metadata(metadata)
    except IOError:
        _log.error("File " + json_name + " not found!")
    return metadata

def prepare_metadata(dic):
    """Collapse all values of this dictionary to strings."""
    for k, v in dic.iteritems():
        try:
            v.sort()
            v = ", ".join(str(x) for x in v)
            dic[k] = v
        except (AttributeError, TypeError):
            pass
    return dic

def valid_pdb_id(pdb_id):
    """Return a valid pdb_id.

    raises a TypeError if the pdb_id argument cannot be converted to a string
    raises a ValueError if the (string representation of the) pdb_id is invalid
    """
    valid = None
    try:
        valid = str(pdb_id)
    except TypeError:
        raise TypeError("PDB identifier should be a string")
    if not re.search(PDB_ID_PAT, valid) or pdb_id is None:
        raise ValueError("Not a valid PDB identifier")
    return valid

def whynot_exists(pdb_id):
    """Return True if a WHY NOT file exists for this pdb_id.

    pdb_id validation is performed by valid_pdb_id
    """
    pdb_id = valid_pdb_id(pdb_id)
    whynot_name = os.path.join(bdb_dir(pdb_id), pdb_id + ".whynot")
    return os.path.isfile(whynot_name)
