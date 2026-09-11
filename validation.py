from datetime import datetime

def validate_amount(amount):
    try:
        amount = float(amount)
    except ValueError:
        return "Invalid amount! Enter a valid amount!"

    return amount

def validate_user_id(user_id):
    if user_id.strip() == "":
        return None
    
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
