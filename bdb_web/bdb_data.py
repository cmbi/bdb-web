from flask import url_for
from bdb_web import app
import json
import os
import logging
_log = logging.getLogger("bdb")

def bdb_dir(pdb_id, bdb_root=app.config["BDB_ROOT"]):
    try:
        return os.path.join(bdb_root, pdb_id[1:3], pdb_id)
    except (AttributeError, TypeError):
      raise TypeError("PDB identifier should be a string")

def bdb_exists(pdb_id):
    return os.path.isfile(bdb_path(pdb_id))

def bdb_path(pdb_id):
    try:
        return os.path.join(bdb_dir(pdb_id), pdb_id + ".bdb")
    except (AttributeError, TypeError):
      raise TypeError("PDB identifier should be a string")

def generate_bdb_url(pdb_id):
    bdb_url = None
    if bdb_exists(pdb_id):
        bdb_url = url_for("download", pdb_id=pdb_id)
    return bdb_url

def generate_whynot_url(pdb_id):
    whynot_url = None
    if whynot_exists(pdb_id):
        try:
            whynot_url = app.config["WHY_NOT_SEARCH_URL"] + str(pdb_id)
        except ValueError:
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

def whynot_exists(pdb_id):
    try:
        whynot_name = os.path.join(bdb_dir(pdb_id), pdb_id + ".whynot")
        return os.path.isfile(whynot_name)
    except (AttributeError, TypeError):
      raise TypeError("PDB identifier should be a string")
