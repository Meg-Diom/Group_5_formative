#!/usr/bin/env python3

def add_an_expense(transactions, user_id, user_name, spending_category, amount, date, description):
    """
    This function, add_an_expense, when called will collect information such as the user_id,
    user_name, spending_category, spending details, amount, date and descriptions from the user
    and save it in a json file.
    """
    new_transaction = {
        "user_id": user_id,
        "user_name": user_name,
        "spending_category": spending_category,
        "amount": amount,
        "date": date,
        "description": description
    }
    transactions.append(new_transaction)
    return transactions

def search_expenses(transactions, user_id):
    """
    search_expenses function is just so that we wouldn't copy/paste code multiple times.
    Since we need to seach documents multiple times, we just write a function for that purpose.
    """
    results = []
    #results stores transactions that have been searched by a particular category, that is, user_id

    for transaction in transactions:
        if transaction["user_id"] == user_id:
            results.append(transaction)

    return results

def find_transaction(transactions, user_id, spending_category, amount):
    result = []
    for transaction in transactions:
        if transaction["user_id"] == user_id and transaction["spending_category"] == spending_category and transaction["amount"] == amount:
            result.append(transaction)
    return result

def view_all_expenses(transactions, user_id):
    """
    view_all_expense function displays the list of all transactions searched by the category
    user_id. 
    """

    results = search_expenses(transactions, user_id)
    
    if not results:
        print("No Transactions yet")
    for result in results:
        print(f"{25*"="}\nTRANSACTION HISTORY\n{25*"="} {result}\n{25*"="}")

def update_an_expense(transactions, user_id, spending_category, amount, field, modify):
    """
    update_an_expence updates a specific transaction searched by two categories. user_id
    and spending datails. The use of the two categories is so that we can find a specific 
    expence and update it. 
    """
    results = find_transaction(transactions, user_id, spending_category, amount)
    field_names = {
        "1": "user_id",
        "2": "user_name",
        "3": "spending_category",
        "4": "amount",
        "5": "date",
        "6": "description"
    }
    fields = field_names.get(field)
    if fields is not None:
        for transaction in results:
                transaction[fields] = modify
    return transactions

def delete_an_expense(transactions, user_id, spending_category, amount):
    """delete_an_expense deletes a spcific transaction when searched using a three keys 
    for specificity."""
    results = find_transaction(transactions, user_id, spending_category, amount)
    
    for transaction in results:
            transactions.remove(transaction)
    return transactions

def expenses_by_category(transactions):
    """
    Search expense by category searches an expense based on the specific filed and value 
    specified.  
    """
    categories = {}

    for transaction in transactions:
        category = transaction["spending_category"]
        amount = transaction["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    return categories

def calculate_total_expenses(transactions):
    """
    total_spendings calculates the expenditure for a particular person based on their 
    spending 
    """
    total = 0
    for transaction in transactions: 
        total = total + transaction["amount"]
    return total

def add_saving_goal(saving_goals, user_id, goal, target_amount, saved_amount, deadline):

    new_goal = {
        "user_id": user_id,
        "goal": goal,
        "target_amount": target_amount,
        "saved_amount": saved_amount,
        "deadline": deadline
    }

    saving_goals.append(new_goal)

    return saving_goals

def find_saving_goal(saving_goals, user_id, goal):
    results = []

    for saving_goal in saving_goals:
        if (saving_goal["user_id"] == user_id
                and saving_goal["goal"] == goal):
            results.append(saving_goal)

    return results

def delete_saving_goal(saving_goals, user_id, goal):

    results = find_saving_goal(saving_goals, user_id, goal)

    for saving_goal in results:
        saving_goals.remove(saving_goal)

    return saving_goals

def update_saving_goal(saving_goals, user_id, goal, field, modify):

    results = find_saving_goal(saving_goals, user_id, goal)

    field_names = {
        "1": "goal",
        "2": "target_amount",
        "3": "saved_amount",
        "4": "deadline"
    }

    field_name = field_names.get(field)

    if field_name is not None:
        for saving_goal in results:
            saving_goal[field_name] = modify

    return saving_goals

def calculate_saving_progress(saving_goals):

    results = []

    for saving_goal in saving_goals:

        progress = (saving_goal["saved_amount"] / saving_goal["target_amount"]) * 100

        results.append({"goal": saving_goal["goal"], "progress": progress})

    return results
