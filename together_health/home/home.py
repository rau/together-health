import os
import sqlite3
from flask import Blueprint
from flask import render_template, send_file, make_response
from flask import current_app, session, request, redirect
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

home_bp = Blueprint(
    'home',
    __name__,
    template_folder='templates',
    static_folder='static'
)

# Routes you to home from both / and index
@home_bp.route('/')
@home_bp.route('/index/')
def index():
    return render_template('index.html')

# Simple about page
@home_bp.route('/about/')
def about():
    return render_template('about.html')

@home_bp.route("/login/", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        db_connect = sqlite3.connect("together_health.db")
        db_connect.row_factory = sqlite3.Row
        db = db_connect.cursor()

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", [request.form.get("username")]).fetchall()


        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["password_hash"], request.form.get("password")):
            return redirect('/?MSG=WRONG_PASSWORD')

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        db_connect.commit()

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@home_bp.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@home_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        db_connect = sqlite3.connect("together_health.db")
        db_connect.row_factory = sqlite3.Row
        db = db_connect.cursor()

        # Remember which user has logged in
        db.execute(
                    '''
                    INSERT INTO preferences DEFAULT VALUES;
                    ''')


        username, password_hash = request.form.get('username'), generate_password_hash(request.form.get('password'))
        name = request.form.get('name')

        if len(db.execute('SELECT * from users WHERE username LIKE ?', [request.form.get('username')]).fetchall()) != 0:
            return redirect('/?MSG=DIFF_USERNAME_PLS')

        db.execute(
                    '''
                    INSERT INTO users (name, username, password_hash) VALUES (?, ?, ?);
                    ''', (name, username, password_hash)
        )

        db_connect.commit()

        return redirect("/login/")
    if request.method == "GET":
        return render_template("register.html")
    return apology("TODO")

@home_bp.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
