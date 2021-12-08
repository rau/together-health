# https://www.cms.gov/CCIIO/Resources/Data-Resources/Downloads/HIOS-RBIS-ICD-03-01-00.pdf
# Above link used to determine database structure, and create healthcare plan data

from sqlite3 import *

def table_setup(db):
    create_plans_table(db)
    create_users_table(db)
    create_users_pref_table(db)
# This table is updated upon registration and queried upon login.
def create_users_table(db):

    return db.execute(
                '''
                CREATE TABLE IF NOT EXISTS users (
                    "id" INTEGER UNIQUE PRIMARY KEY,
                    "name" TEXT NOT NULL,
                    "username" TEXT NOT NULL,
                    "password_hash" TEXT NOT NULL
                );
                '''
            )

# This function updates a table with dummy data.
def create_plans_table(db):

    x = db.execute(
                '''
                CREATE TABLE IF NOT EXISTS plans (
                    "plan_id" INTEGER UNIQUE PRIMARY KEY,
                    "out_of_area" BOOLEAN DEFAULT false,
                    "tobacco" BOOLEAN DEFAULT false,
                    "disease" BOOLEAN DEFAULT false,
                    "dental" BOOLEAN DEFAULT false,
                    "copay" INTEGER NOT NULL,
                    "individual" INTEGER NOT NULL,
                    "couple" INTEGER NOT NULL,
                    "dependent" INTEGER NOT NULL
                );
                '''
            ).fetchall()
    # ONLY RUN ONCE, IN CASE THE SAMPLE DATA IS LOST!
    populate_plans_table(db)

def populate_plans_table(db):

    db.execute(
                '''
                INSERT INTO plans (
                    out_of_area,
                    tobacco,
                    disease,
                    dental,

                    copay,

                    individual,
                    couple,
                    dependent
                )
                VALUES
                (false, false, false, false, 200, 500, 1000, 300),
                (false, false, false, false, 400, 600, 750, 80),



                (false, true, false, false, 250, 800, 1300, 350),

                (false, false, true, false, 250, 900, 1300, 100),
                (false, false, true, false, 1000, 900, 1300, 100),
                (false, false, true, false, 400, 1050, 1650, 250),

                (false, false, false, true, 300, 450, 800, 400),
                (false, false, false, true, 1800, 250, 500, 250),

                (true, false, false, false, 750, 800, 1000, 100),
                (true, false, false, false, 1350, 350, 650, 300),
                (true, false, false, false, 350, 600, 1200, 400),



                (true, true, false, false, 2000, 200, 300, 100),
                (true, true, false, false, 200, 800, 1600, 500),

                (true, false, true, false, 1450, 400, 800, 100),
                (true, false, true, false, 1450, 500, 1000, 200),
                (true, false, true, false, 1600, 300, 600, 300),

                (true, false, false, true, 450, 350, 650, 250),
                (true, false, false, true, 750, 450, 1000, 100),
                (true, false, false, true, 550, 400, 500, 200),

                (false, true, true, false, 1000, 200, 300, 100),

                (false, true, false, true, 500, 300, 500, 300),

                (false, false, true, true, 1400, 450, 1000, 250),
                (false, false, true, true, 1150, 600, 1300, 350),



                (true, true, true, false, 1200, 650, 900, 100),
                (true, true, true, false, 800, 1000, 1300, 200),
                (true, true, true, false, 950, 850, 1250, 300),

                (true, false, true, true, 800, 850, 750, 300),

                (true, true, false, true, 250, 300, 600, 300),
                (true, true, false, true, 500, 100, 200, 400),

                (false, true, true, true, 400, 700, 750, 200),



                (true, true, true, true, 500, 1000, 1250, 300),
                (true, true, true, true, 1250, 850, 1000, 400);
                '''
            )

def load_plans(db):

    plans_dict = db.execute("SELECT * FROM plans;").fetchall()

    return plans_dict

# This is only a test function; the real version will have this as the preferences of the current user using the session id.
def load_user_preferences(db):

    pref_dict = db.execute("SELECT * FROM preferences;").fetchall()

    return pref_dict

# This table is updated (or receives a new entry) when the preferences are submitted
def create_users_pref_table(db):

    x = db.execute(
                '''
                CREATE TABLE IF NOT EXISTS preferences (
                    "user_id" INTEGER UNIQUE PRIMARY KEY,

                    "married" BOOLEAN DEFAULT false,
                    "dependents" INTEGER DEFAULT 0,

                    "tobacco" BOOLEAN DEFAULT false,
                    "preexisting" BOOLEAN DEFAULT false,
                    "dental" BOOLEAN DEFAULT false,
                    "travel" BOOLEAN DEFAULT false,

                    "monthly_budget_high" INTEGER DEFAULT 3000,

                    "copay_high" INTEGER DEFAULT 3000
                );
                '''
            ).fetchall()


    # if len(x) == 0:
    #     create_sample_preferences(db)

# def create_sample_preferences(db):
#
#     db.execute(
#                 '''
#                 INSERT INTO preferences (
#                     married,
#                     dependents,
#
#                     tobacco,
#                     preexisting,
#                     dental,
#                     travel,
#
#                     monthly_budget_high,
#
#                     copay_high
#                 )
#                 VALUES
#                 (true, 3, false, false, true, false, 1500, 500),
#                 (true, 0, true, true, true, false, 800, 1000),
#                 (true, 5, false, false, true, false, 3000, 2000),
#                 (true, 1, false, true, true, false, 800, 400),
#
#                 (true, 2, false, false, true, true, 1000, 1500),
#                 (true, 1, false, false, true, true, 900, 900),
#                 (true, 0, false, true, true, true, 1200, 400),
#                 (false, 3, false, false, false, false, 600, 2500),
#
#                 (false, 0, false, false, true, true, 1500, 500),
#                 (false, 5, false, false, true, false, 1500, 1500),
#                 (false, 1, false, false, false, true, 3000, 3000),
#                 (false, 1, false, false, true, false, 600, 800);
#                 '''
#             )
