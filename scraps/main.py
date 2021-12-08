from utils.manage_tables import *
from utils.scoring import *
import sqlite3

db_connect = sqlite3.connect("/Users/sbmynam/Documents/CS50/scraps/data/together-health.db")

db_connect.row_factory = sqlite3.Row

db = db_connect.cursor()

if __name__ == "__main__":
    # create_plans_table(db)
    # create_users_pref_table(db)

    db_connect.commit()

    plans = load_plans(db)

    # replace this with the 
    preference = load_user_preferences(db)[0]
    print(dict(zip(preference.keys(), [i for i in preference])))
    print("")
    print(rank_plans(preference, plans))