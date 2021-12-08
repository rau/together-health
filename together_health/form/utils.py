from flask import session
import sqlite3

def submit_form(request):
    married = True if request.form.get('married') == 'on' else False
    smoke = True if request.form.get('smoke') == 'on' else False
    service = True if request.form.get('service') == 'on' else False
    condition = True if request.form.get('condition') == 'on' else False
    dental = True if request.form.get('dental') == 'on' else False
    copay = request.form.get('copay')
    dependents = request.form.get('dependents')
    prem = request.form.get('prem')
    print('askdjaslkdja')
    print(prem)
    db_connect = sqlite3.connect("together_health.db")
    db_connect.row_factory = sqlite3.Row
    db = db_connect.cursor()

    db.execute(
                '''
                UPDATE preferences SET
                    married = ?,
                    dependents = ?,
                    tobacco = ?,
                    preexisting = ?,
                    dental = ?,
                    travel = ?,
                    monthly_budget_high = ?,
                    copay_high = ?
                 WHERE user_id = ?;
                ''', (married, dependents, smoke, condition, dental, service, request.form.get('prem'), copay, session['user_id'])
            )

    db_connect.commit()
