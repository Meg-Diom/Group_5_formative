#!/usr/bin/env python3

"""
Vlaidation module has functions such as validate_amount to validate the amount,
validate_user_id to validate the user id, validate_user_name to validate user name,
validate_spending_category, tovalidate category, validate_date, to validate the date
to a particular date format, validate_description, sothat it doesn't take empty spaces and
invalid inputs, validate_goal, to reject empty spaces and validate_target_amount to validate
the target amount
"""

from datetime import datetime

def validate_amount(amount):
    try:
        amount = float(amount)
    except ValueError:
        return "Invalid amount! Enter a valid amount!"

    return amount

def validate_user_id(user_id):
    if user_id.strip() == "":
        return 
    
    return user_id.strip().lower()


def validate_user_name(user_name):

    name = []

    for i in user_name:
        if i.isalpha() or i == " ":
            name.append(i)
        else:
            return None

    return "".join(name)


def validate_spending_category(spending_category):
    if spending_category.strip() == "":
        return None
    return spending_category

def validate_date(date):
    if date.strip() == "":
        return None
    try:
        date = datetime.strptime(date, "%d/%m/%Y")
        return date.strftime("%d/%m/%Y")
    except ValueError:
        return None

def validate_description(description):
    if description.strip() == "":
        return None
    return description.strip()

def validate_goal(goal):
    goal = goal.strip()

    if goal == "":
        return None

    return goal

def validate_target_amount(amount):
    try:
        amount = float(amount)
    except ValueError:
        return None

    if amount <= 0:
        return None

    return amount
