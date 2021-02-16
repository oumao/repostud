from flask import Blueprint

assign = Blueprint('assign', __name__)

from . import routes