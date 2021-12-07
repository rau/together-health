import os
from flask import Blueprint
from flask import render_template, send_file, make_response
from flask import current_app

admin_bp = Blueprint(
    'admin',
    __name__,
    template_folder='templates',
    static_folder='static'
)

@home_bp.route('/admin/')
def index():
    return render_template('admin.html')
