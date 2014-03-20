from bdb_web.bdb_data import bdb_dir
from nose.tools import raises

@raises(TypeError)
def test_bdb_dir_float():
    bdb_dir(float(1), bdb_root="")

@raises(TypeError)
def test_bdb_dir_int():
    bdb_dir(int(1), bdb_root="")

@raises(TypeError)
def test_bdb_dir_none():
    bdb_dir(None, bdb_root="")


