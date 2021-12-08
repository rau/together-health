# This is a variation on the distance function in a 3D space (copay, monthly rate, amenities)
import math

# Given a preference set and a healthcare plan, determines the match between them. This will be a value from 1 to the square root of 6 (at max)
def score(preferences, plan):

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
    return plans[:min(5, len(plans))]
