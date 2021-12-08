import sqlite3

def submit_form(request):
    married = True if request.form.get('married') == 'on' else False
    smoke = True if request.form.get('smoke') == 'on' else False
    service = True if request.form.get('service') == 'on' else False
    condition = True if request.form.get('condition') == 'on' else False
    dental = True if request.form.get('dental') == 'on' else False
    copay = request.form.get('copay')
    dependents = request.form.get('dependents')
    premium = request.form.get('premium')

    db_connect = sqlite3.connect("together_health.db")
    db_connect.row_factory = sqlite3.Row
    db = db_connect.cursor()

    db.execute(
                '''
                INSERT INTO preferences (
                    married,
                    dependents,
                    smoke,
                    preexisting,
                    dental,
                    travel,
                    monthly_budget_high,
                    copay_high
                )
                VALUES
                (?, ?, ?, ?, ?, ?, ?, ?);
                ''', (married, dependents, smoke, condition, dental, service, premium, copay)
            )

    db.commit()
