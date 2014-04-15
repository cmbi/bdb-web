from wtforms import Form, TextField, validators

from bdb_data import PDB_ID_PAT


class SearchForm(Form):
    message = "Please provide a valid PDB identifier."
    name = TextField(
            label="Search a BDB entry",
            validators = [validators.Regexp(
                regex=PDB_ID_PAT,
                message=message)],
            description = {
                    "size": 15,
                    "results": 5,
                    "placeholder": "Enter a PDB code",
                    "pattern": "^[A-Za-z0-9]{4}$"})
