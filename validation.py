from datetime import  datetime

def validate_amount(amount):
    """
    Validate and convert an expense amount.
    """
    try:
        amount = float(amount)
    except ValueError:
        return "Invalid amount! Enter a valid amount!"

    return amount

def validate_user_id(user_id):
    """ validate user ID."""
    if user_id.strip() == "":
        return None
    
    return user_id.strip().lower()


def validate_user_name(user_name):
    """ Validate a user's name. The name may contain only alphabetic characters and spaces."""
    name = []

    for i in user_name:
        if i.isalpha() or i == " ":
            name.append(i)
        else:
            return None

    return "".join(name)


def validate_spending_category(spending_category):
    """ Validate  an expense category. """
    if spending_category.strip() == "":
        return None
    return spending_category

def validate_date(date):
    """ Validate the transaction date."""
    if date.strip() == "":
        return None
    try:
        date = datetime.strptime(date, "%d/%m/%Y")
        return date.strftime("%d/%m/%Y")
    except ValueError:
        return None

def validate_description(description):
    """ Validate a transaction description."""
    if description.strip() == "":
        return None
    return description.strip()
