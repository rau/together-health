"""
The heart of the app, this file creates the Flask app, and initializes all of the extensions it utilizes.

We use sqlite3 as our db but we don't use an ORM. It was easier for us to just connect directly.

We still haven't implemented flask_talisman and flask_seasurf for web attack protection. This is on our next-up list.

"""

import os, sys
from flask import Flask, request
from flask_seasurf import SeaSurf
from dotenv import load_dotenv
load_dotenv()

sys.path.append(os.path.join(os.path.dirname(__file__)))

csrf = SeaSurf()

def create_app():
    app = Flask(__name__)
    set_config(app)
    init_apps(app)
    with app.app_context():
        register_blueprints(app)
        return app

# Sets the overall Flask app config from the config file.
def set_config(app):
    from together_health.config import Config
    app.config.from_object(Config)

# Initializes all extensions
def init_apps(app):
    csrf.init_app(app)

# Registers blueprints for flask app
def register_blueprints(app):
    from together_health.form import form
    from together_health.home import home

    app.register_blueprint(form.form_bp)
    app.register_blueprint(home.home_bp)
