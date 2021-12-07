import os
from flask import Blueprint
from flask import render_template, send_file, make_response
from flask import current_app

home_bp = Blueprint(
    'home',
    __name__,
    template_folder='templates',
    static_folder='static'
)

@home_bp.route('/')
def index():
    return render_template('index.html')

@home_bp.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
