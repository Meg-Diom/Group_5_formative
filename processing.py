#!/usr/bin/env python3

# Adds a new expense transaction with user info, category, amount, date, and description
def add_an_expense(transactions, user_id, user_name, spending_category, amount, date, description):
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

# Searches for expenses by user_id to avoid code duplication across the application
def search_expenses(transactions, user_id):
    results = []
    # Results stores transactions filtered by user_id

    for transaction in transactions:
        if transaction["user_id"] == user_id:
            results.append(transaction)

    return results

# Finds a specific transaction by user_id, spending_category, and amount
def find_transaction(transactions, user_id, spending_category, amount):
    result = []
    for transaction in transactions:
        if transaction["user_id"] == user_id and transaction["spending_category"] == spending_category and transaction["amount"] == amount:
            result.append(transaction)
    return result

# Displays all transactions for a given user_id
def view_all_expenses(transactions, user_id):

    results = search_expenses(transactions, user_id)
    
    if not results:
        print("No Transactions yet")
    for result in results:
        print(f"{25*"="}\nTRANSACTION HISTORY\n{25*"="} {result}\n{25*"="}")

# Updates a specific transaction field searched by user_id, spending_category, and amount
def update_an_expense(transactions, user_id, spending_category, amount, field, modify):
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

# Deletes a specific transaction using user_id, spending_category, and amount for specificity
def delete_an_expense(transactions, user_id, spending_category, amount):
    results = find_transaction(transactions, user_id, spending_category, amount)
    
    for transaction in results:
            transactions.remove(transaction)
    return transactions

# Aggregates expenses by category and returns a dictionary of {category: total_amount}
def expenses_by_category(transactions):
    categories = {}

    for transaction in transactions:
        category = transaction["spending_category"]
        amount = float(transaction["amount"])

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    return categories

# Calculates the total sum of all expenses
def calculate_total_expenses(transactions):
    total = 0
    for transaction in transactions: 
        total = total + float(transaction["amount"])
    return total

# Adds a new saving goal with user_id, goal name, target amount, saved amount, and deadline
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

# Finds saving goals matching user_id and goal name
def find_saving_goal(saving_goals, user_id, goal):
    results = []

    for saving_goal in saving_goals:
        if (saving_goal["user_id"] == user_id
                and saving_goal["goal"] == goal):
            results.append(saving_goal)

    return results

# Deletes a saving goal matching user_id and goal name
def delete_saving_goal(saving_goals, user_id, goal):

    results = find_saving_goal(saving_goals, user_id, goal)

    for saving_goal in results:
        saving_goals.remove(saving_goal)

    return saving_goals

# Updates a specific field in a saving goal (goal, target_amount, saved_amount, or deadline)
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

# Calculates progress percentage for all saving goals
def calculate_saving_progress(saving_goals):

    results = []

    for saving_goal in saving_goals:

        progress = (float(saving_goal["saved_amount"]) / float(saving_goal["target_amount"])) * 100

        results.append({"goal": saving_goal["goal"], "progress": progress})

    return results
