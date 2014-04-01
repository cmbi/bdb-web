from bdb_web.bdb_data import bdb_dir, bdb_path, generate_bdb_url,\
parse_bdb_metadata, prepare_metadata, valid_pdb_id
from mock import patch
from nose.tools import assert_true, eq_, raises

def test_bdb_dir():
    expected = "/foo/ba/1bar"
    actual = bdb_dir("1bar", bdb_root="/foo")
    eq_(actual, expected)

@patch("bdb_web.bdb_data.bdb_dir", return_value="/foo/ba/1bar")
def test_bdb_path(*args):
    expected = "/foo/ba/1bar/1bar.bdb"
    actual = bdb_path("1bar")
    eq_(actual, expected)

@patch("bdb_web.bdb_data.bdb_exists", return_value=False)
def test_generate_bdb_url_none(*args):
    expected = None
    actual = generate_bdb_url("1bar")
    eq_(actual, expected)

#TODO def test_generate_bdb_url:
#TODO def test_generate_whynot_url:

@patch("bdb_web.bdb_data.bdb_dir", return_value="/foo/ba/1bar")
def test_parse_bdb_metadata(*args):
    expected = None
    actual = parse_bdb_metadata("1bar")
    eq_(actual, expected)

@patch("bdb_web.bdb_data.bdb_dir", raises=TypeError)
def test_parse_bdb_metadata(*args):
    expected = None
    actual = parse_bdb_metadata("1bar")
    eq_(actual, expected)

@patch("bdb_web.bdb_data.bdb_dir", raises=ValueError)
def test_parse_bdb_metadata(*args):
    expected = None
    actual = parse_bdb_metadata("1bar")
    eq_(actual, expected)

def test_prepare_metadata():
    dic = {"ints": [1, 2, 3], "strs": ["a", "b", "c"], "none": None}
    expected = {"ints": "1, 2, 3", "strs": "a, b, c", "none": None}
    actual = prepare_metadata(dic=dic)
    eq_(actual, expected)

@raises(ValueError)
def test_valid_pdb_id_float():
    valid_pdb_id(float(1))

@raises(ValueError)
def test_valid_pdb_id_int():
    valid_pdb_id(int(1))

@raises(TypeError)
def test_valid_pdb_id_list():
    valid_pdb_id(list(1))

@raises(ValueError)
def test_valid_pdb_id_none():
    valid_pdb_id(None)

@raises(ValueError)
def test_valid_pdb_id_too_long():
    valid_pdb_id("aaaaa")

@raises(ValueError)
def test_valid_pdb_id_too_short():
    valid_pdb_id("aaa")

@raises(ValueError)
def test_valid_pdb_id_wrong_char():
    valid_pdb_id("aaa$")

def test_valid_pdb_id():
    assert_true(valid_pdb_id("1crn"))

