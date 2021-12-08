import os
from flask import Blueprint
from flask import render_template, send_file, make_response
from flask import current_app, session, request

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

@home_bp.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

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

        if not request.form.get("username"):
            return apology("must provide username", 400)
        elif not request.form.get("password"):
            return apology("must provide password", 400)
        elif not request.form.get("password") == request.form.get('confirmation'):
            return apology('must match passwords', 400)
        elif len(db.execute('SELECT * from users WHERE username LIKE ?', request.form.get('username'))) != 0:
            return apology('must provide unique username', 400)

        username, password, confirmation = request.form.get('username'), generate_password_hash(request.form.get('password')), request.form.get('confirmation')
        p_k = db.execute('INSERT INTO users (username, hash) VALUES (?, ?)', username, password)
        return render_template("login.html")
    if request.method == "GET":
        return render_template("register.html")
    return apology("TODO")

@home_bp.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
