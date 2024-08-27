import json
from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/healthz', methods=['GET'])
def index():
    return "<body style='background: black;'><p style='color: white;'>Healthy!</p></body>"
