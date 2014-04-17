from wtforms import TextField, validators
from wtforms.validators import Regexp
from flask_wtf import Form

from bdb_data import PDB_ID_PAT


class SearchForm(Form):
    message = "Please provide a valid PDB identifier."
    name = TextField(
            label="Search a BDB entry",
            validators = [Regexp(regex=PDB_ID_PAT, message=message)],
            description = {"size": 15, "results": 5, "required": "required",
                "placeholder": "Enter a PDB code", "pattern": PDB_ID_PAT})
