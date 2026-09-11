#!/usr/bin/env python3

# Validation module with functions to validate user inputs: amount, user_id, user_name, 
# spending_category, date, description, goal, and target_amount

from datetime import datetime

# Validates amount as a float value
def validate_amount(amount):
    try:
        amount = float(amount)
    except ValueError:
        return "Invalid amount! Enter a valid amount!"

    return amount

# Validates user_id by stripping whitespace and converting to lowercase
def validate_user_id(user_id):
    if user_id.strip() == "":
        return 
    
    return user_id.strip().lower()


# Validates user_name to only contain alphabetic characters and spaces
def validate_user_name(user_name):

    name = []

    for i in user_name:
        if i.isalpha() or i == " ":
            name.append(i)
        else:
            return None

    return "".join(name)


# Validates spending_category is not empty
def validate_spending_category(spending_category):
    if spending_category.strip() == "":
        return None
    return spending_category

# Validates date format is dd/mm/yyyy
def validate_date(date):
    if date.strip() == "":
        return None
    try:
        date = datetime.strptime(date, "%d/%m/%Y")
        return date.strftime("%d/%m/%Y")
    except ValueError:
        return None

# Validates description is not empty
def validate_description(description):
    if description.strip() == "":
        return None
    return description.strip()

# Validates goal is not empty after stripping whitespace
def validate_goal(goal):
    goal = goal.strip()

    if goal == "":
        return None

    return goal

# Validates target_amount is a float and greater than 0
def validate_target_amount(amount):
    try:
        amount = float(amount)
    except ValueError:
        return None

    if amount <= 0:
        return None

    return amount
