from flask import url_for
from bdb_web import app
import json
import os
import re

import logging
_log = logging.getLogger("bdb")

PDB_ID_PAT = re.compile(r"^[0-9a-zA-Z]{4}$")

def bdb_dir(pdb_id, bdb_root=app.config["BDB_ROOT"]):
    if valid_pdb_id(pdb_id):
        return os.path.join(bdb_root, pdb_id[1:3], pdb_id)

def bdb_exists(pdb_id):
    return os.path.isfile(bdb_path(pdb_id.lower()))

def bdb_path(pdb_id):
    if valid_pdb_id(pdb_id):
        return os.path.join(bdb_dir(pdb_id), pdb_id + ".bdb")

def generate_bdb_url(pdb_id):
    bdb_url = None
    if bdb_exists(pdb_id):
        bdb_url = url_for("download", pdb_id=pdb_id)
    return bdb_url

def generate_whynot_url(pdb_id):
    whynot_url = None
    if valid_pdb_id(pdb_id) and whynot_exists(pdb_id):
            whynot_url = app.config["WHY_NOT_SEARCH_URL"] + str(pdb_id)
            raise ValueError("PDB identifier should be a string")
    return whynot_url

def parse_bdb_metadata(pdb_id):
    """Parse BDB file metadata in json format."""
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
    for k, v in dic.iteritems():
        try:
            v.sort()
            v = ", ".join(str(x) for x in v)
            dic[k] = v
        except (AttributeError, TypeError):
            pass
    return dic

def valid_pdb_id(pdb_id):
    if not isinstance(pdb_id, str):
        raise TypeError("PDB identifier should be a string")
    if not re.search(PDB_ID_PAT, pdb_id):
        raise ValueError("Not a valid PDB identifier")
    return True

def whynot_exists(pdb_id):
    whynot_exists = False
    if valid_pdb_id(pdb_id):
        whynot_name = os.path.join(bdb_dir(pdb_id), pdb_id + ".whynot")
        whynot_exists = os.path.isfile(whynot_name)
    return whynot_exists
