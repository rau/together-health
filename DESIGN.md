A “design document” for your project in the form of a Markdown file called DESIGN.md that discusses, technically, how you implemented your project and why you made the design decisions you did. Your design document should be at least several paragraphs in length. Whereas your documentation is meant to be a user’s manual, consider your design document your opportunity to give the staff a technical tour of your project underneath its hood.

# TogetherHealth

## Purpose

The overarching purpose of our website is to allow users to register and login an account which allows them to submit information forms about themselves. First, we have three databases involved in our project. One table consists of id, name, username, and a password. Another table consists of a plan_id, out_of_area boolean, tobacco boolean, disease boolean, dental boolean, copay integer, individual integer, couple interger, and dependent integer. A plan_id refers to a unique identifier for an insurance plan. out_of_area refers to whether or not the individual is within the coverage area of the insurance plan. tobacco boolean refers to whether or not an individual would be corried

## Objectives:

These objectives

- Let users register and login to the site.
- Allow them to specify their healthcare needs.
- Recommend and show them plans  that most closely align with their needs.

## Design Considerations:

### Website Architecture (Raunak)

Blueprints and Flask

### The Login/Register Pages (Raunak and Saketh)



### The Plan Form (Khoi)



### Letting Users See Their Matches (Khoi)



### The Sample Data (Saketh and Khoi)

The sample data was constructed using the information detailed in [this PDF](https://www.cms.gov/CCIIO/Resources/Data-Resources/Downloads/HIOS-RBIS-ICD-03-01-00.pdf), which contains information on the type of data that healthcare plans often hold. In order to simplify the data, we created dummy data based on the information contained in the PDF. 

The sample data is structured as it is in order to accurately represent the 

The schema for the the database is as follows:

```
CREATE TABLE plans (
                    "plan_id" INTEGER UNIQUE PRIMARY KEY,
                    "out_of_area" BOOLEAN DEFAULT false,
                    "tobacco" BOOLEAN DEFAULT false,
                    "disease" BOOLEAN DEFAULT false,
                    "dental" BOOLEAN DEFAULT false,
                    "copay" INTEGER NOT NULL,
                    "individual" INTEGER NOT NULL,
                    "couple" INTEGER NOT NULL,
                    "dependent" INTEGER NOT NULL
                )
                
CREATE TABLE preferences (
                    "user_id" INTEGER UNIQUE PRIMARY KEY,
                    "married" BOOLEAN DEFAULT false,
                    "dependents" INTEGER DEFAULT 0,
                    "tobacco" BOOLEAN DEFAULT false, 
                    "preexisting" BOOLEAN DEFAULT false, 
                    "dental" BOOLEAN DEFAULT false,
                    "travel" BOOLEAN DEFAULT false,
                    "monthly_budget_high" INTEGER DEFAULT 3000,
                    "copay_high" INTEGER DEFAULT 3000
                )
```

### The Algorithm (Saketh)

The algorithm essentially decomposes the users' data into 3 axes; their needs for copay (which is a function of their expected risk), the risk taken by the insurance carrier (some people may need a dental plan, or coverage for other conditions like diseases or smoking), and the monthly premium (affordability). It maps the data into a space, where it then calculates the length of three normalized vecotrs and sums them; the norm of this vecotr is the"distance" between a patient and a plan; the smaller this distance, the better.

We chose this algorithm because it is applicable to many other applications (such as roommate matching) and will help us with the future development of this app, as real healthcare plans may have factors that add more axes or complicated calculations to the graph.
