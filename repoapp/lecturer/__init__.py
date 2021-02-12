from flask import Blueprint

lecturer = Blueprint('lecturer', __name__)

from . import routes