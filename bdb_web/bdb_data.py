import logging
_log = logging.getLogger("bdb-web")

import json
import os
import re

from flask import url_for

from bdb_web import app


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
    try:
        if bdb_exists(pdb_id):
            bdb_url = url_for("download", pdb_id=pdb_id)
    except ValueError as e:
        _log.debug(e)
    except TypeError as e:
        _log.error(e)
    return bdb_url


def generate_pdb_url(pdb_id):
    """Return a url to the PDB website for this pdb_id.

    Also return a url if the pdb_id is nonsense. We let
    the (RCSB) website figure out if the page exists.

    Return None if a PDB url can somehow not be created.
    """
    pdb_url = None
    try:
        pdb_url = app.config["PDB_SEARCH_URL"] + str(pdb_id)
    except TypeError:
        raise TypeError("PDB identifier should be a string")
#    except ValueError as e:
#        _log.error(e)
    return pdb_url


def generate_tlsanl_log_url(pdb_id):
    """Return a url for downloading the TLSANL log file if it exists, else None.

    pdb_id validation is performed by valid_pdb_id
    """
    tlsanl_log_url = None
    try:
        if tlsanl_log_exists(pdb_id):
            tlsanl_log_url = url_for("tlsanl_log", pdb_id=pdb_id)
    except ValueError as e:
        _log.debug(e)
    except TypeError as e:
        _log.error(e)

    return tlsanl_log_url


def generate_whynot_url(pdb_id):
    """Return a url to the WHY NOT file for this pdb_id.

    Also return a url if the WHY NOT file does not exist locally. We let
    the WHY NOT website figure out why there is no WHY NOT BDB file.

    Return None if a WHY NOT url can somehow not be created.
    """
    whynot_url = None
    try:
        whynot_url = app.config["WHY_NOT_SEARCH_URL"] + str(pdb_id)
    except TypeError:
        raise TypeError("PDB identifier should be a string")
    return whynot_url


def parse_bdb_metadata(pdb_id):
    """Parse BDB file metadata in json format.

    pdb_id validation is performed by valid_pdb_id
    """
    metadata = None
    try:
        json_name = os.path.join(bdb_dir(pdb_id), pdb_id + ".json")
        if not os.path.isfile(json_name):
            _log.debug("File " + json_name + " not found!")
            return None
        with open(json_name, "r") as jf:
            metadata = json.load(jf)
            metadata = prepare_metadata(metadata)
    except ValueError as e:
        _log.debug(e)
    except IOError as e:
        _log.error(e)
    except TypeError as e:
        _log.error(e)
    return metadata


def pdb_path(pdb_id, pdb_root=app.config["PDB_ROOT"]):
    """Return the path to this PDB id.

    pdb_id validation is performed by valid_pdb_id
    """
    pdb_id = valid_pdb_id(pdb_id)
    return os.path.join(pdb_root, "pdb{}.ent".format(pdb_id))


def prepare_metadata(dic):
    """Collapse all values of this dictionary to strings."""
    for k, v in dic.iteritems():
        try:
            if isinstance(v, (list, tuple)):
                v = ", ".join(str(x) for x in v)
                dic[k] = v
        except (AssertionError, TypeError):
            pass
    return dic


def tlsanl_log_exists(pdb_id):
    """Return True if this the TLSANL log exists.

    pdb_id validation is performed by valid_pdb_id
    """
    return os.path.isfile(tlsanl_log_path(pdb_id.lower()))


def tlsanl_log_path(pdb_id):
    """Return the path to this TLSANL log.

    pdb_id validation is performed by valid_pdb_id
    """
    return os.path.join(bdb_dir(pdb_id), "tlsanl.log")


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
        raise ValueError("Not a valid PDB identifier: {}".format(pdb_id))
    return valid


def whynot_exists(pdb_id):
    """Return True if a WHY NOT file exists for this pdb_id.

    pdb_id validation is performed by valid_pdb_id
    """
    pdb_id = valid_pdb_id(pdb_id)
    whynot_name = os.path.join(bdb_dir(pdb_id), pdb_id + ".whynot")
    return os.path.isfile(whynot_name)
