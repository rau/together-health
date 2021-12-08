import os
import sys
import sqlite3
import math
from flask import Blueprint
from flask import render_template, send_file, make_response
from flask import current_app, request, session
from together_health.form.utils import submit_form
from together_health.form.scripts import *


sys.path.append(os.path.join(os.path.dirname(__file__)))

form_bp = Blueprint(
    'form',
    __name__,
    template_folder='templates',
    static_folder='static'
)

@form_bp.route('/admin/')
def index():
    return render_template('admin.html')

@form_bp.route('/form/', methods=["GET", "POST"])
def form():
    if request.method == 'POST':
        print(session['user_id'])
        submit_form(request)
        return render_template('form.html')
    if request.method == 'GET':
        db_connect = sqlite3.connect("together_health.db")
        db_connect.row_factory = sqlite3.Row
        db = db_connect.cursor()
        x = create_users_table(db)
        print(x)
        create_plans_table(db)
        create_users_pref_table(db)
        db_connect.commit()
        return render_template('form.html')


# This function gets the plans that are most applicable to the user via an algorithm that reduces the patient's data into three dimensions. It tries to match the expectation for copay, monthly rate, and desired services.
def get_plans():
    # We used this to create dummy data. If the dummy data is lost, then you can uncomment these functions and re run them. We don't need them anymore so we have them commented out.
    # create_plans_table(db)
    # create_users_pref_table(db)

    db_connect.commit()

    preference = load_user_preferences(db)[0]
    print(dict(zip(preference.keys(), [i for i in preference])))
    print("")
    print(rank_plans(preference, plans))

# Given a preference set and a healthcare plan, determines the match between them. This will be a value from 1 to the square root of 6 (at max)

def score(preferences, plan):
    # This is a variation on the distance function in a 3D space (copay, monthly rate, amenities)

    copay_diff = max(preferences["copay_high"] - plan["copay"], 0)/preferences["copay_high"]

    monthly_rate = plan["couple"] if preferences["married"] else plan["individual"]
    monthly_rate += plan["dependent"] * preferences["dependents"]
    rate_diff = max(preferences["monthly_budget_high"] - monthly_rate, 0)/preferences["monthly_budget_high"]

    # Proper services is weighted 2 times as heavily, as an example.
    services = ["tobacco", "dental", "out_of_area", "disease"]
    service_preferences = ["tobacco", "dental", "travel", "preexisting"]
    service_diff = 0
    for i in range(len(services)):
        service_diff += 1/2 * (plan[services[i]] - preferences[service_preferences[i]]) ** 2

    return math.sqrt(copay_diff ** 2 + rate_diff ** 2 + service_diff ** 2)

# Returns the 5 most applicable plans!
def rank_plans(preferences, plans):
    plans.sort(key=lambda x: score(preferences, x))

    top_plans = plans[:min(5, len(plans))]
    return [dict(zip(x.keys(), [i for i in x])) for x in top_plans]
