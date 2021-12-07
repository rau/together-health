import os
from flask import Blueprint
from flask import render_template, send_file, make_response
from flask import current_app

form_bp = Blueprint(
    'form',
    __name__,
    template_folder='templates',
    static_folder='static'
)

@home_bp.route('/form/')
def index():
    return render_template('form.html')
