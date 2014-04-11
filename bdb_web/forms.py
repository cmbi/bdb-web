from wtforms import Form, TextField, validators

from bdb_data import PDB_ID_PAT

class SearchForm(Form):
    message = "Please provide a valid PDB identifier."
    name = TextField("Search a BDB entry",
            [validators.Regexp(regex=PDB_ID_PAT, message=message)])
