"""
The heart of the app, this file creates the Flask app, and initializes all of the extensions it utilizes.

We use SQLAlchemy as our ORM, and we use MySQL as our database.
We use flask_migrate to manage database migrations.
We use flask_login and flask_bcrypt for login management on the admin dashboard.

We still haven't implemented flask_talisman and flask_seasurf for web attack protection.

"""

import os, sys
from flask import Flask, request
from flask_seasurf import SeaSurf
from dotenv import load_dotenv
load_dotenv()

sys.path.append(os.path.join(os.path.dirname(__file__)))

migrate = Migrate()
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
    from together-health.config import Config
    app.config.from_object(Config)

# Initializes all extensions
def init_apps(app):
    csrf.init_app(app)

# Registers blueprints for flask app
def register_blueprints(app):
    from together-health.form import form
    from together-health.home import home
    from together-health.admin import admin

    app.register_blueprint(form.form_bp)
    app.register_blueprint(home.home_bp)
    app.register_blueprint(admin.admin_bp)
