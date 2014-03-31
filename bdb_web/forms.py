from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import Regexp

from bdb_data import PDB_ID_PAT

class SearchForm(Form):
    message = "Please provide a valid PDB identifier."
    name = TextField("search", validators=[Regexp(regex=PDB_ID_PAT,
                                                  message=message)])
