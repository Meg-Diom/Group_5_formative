#!/usr/bin/env python3
"""Personal Budget Tracker CLI

This module provides the command-line interface for a simple personal
budget tracker. It relies on the following modules which handle
persistence, processing and validation logic:

- data_store: load_data() and save_data() for loading/saving transactions
- processing: functions for adding, finding, updating, deleting and
  aggregating transactions
- validation: input validation helpers

The program displays a menu and allows the user to add, view, update,
delete and search expenses, as well as view totals and category totals.
The program also displays a munu for managing saving goals

Usage:
    python main.py

Note: The file keeps the original CLI behaviour and only wraps it in a
`main()` function so it can be imported without running immediately.
"""

import data_store
import processing
import validation


def main():
    """Run the Personal Budget Tracker command-line interface.

    The function loads stored transactions, displays an interactive menu
    and reacts to user choices to add, list, update, delete and search
    expenses. All user input is validated using helpers from the
    `validation` module and changes are persisted through `data_store`.

    There are no parameters and the function returns None. It runs an
    infinite loop until the user chooses the "Exit" option.
    """

    # Load persisted data (creates a dict with a "transactions" list)
    data = data_store.load_data()
    transactions = data["transactions"]
    saving_goals = data["saving_goals"]

    # Main interactive loop — repeats until the user selects Exit
    while True:
        # Print the menu
        print(40 * "-")
        print("===== PERSONAL BUDGET TRACKER =====")
        print(40 * "-")
        print("1. Add expense\n2. View expense\n3. Update expense\n4. Delete expense")
        print("5. Search expense\n6. Show total expense\n7. Show expense by category\n8. Manage saving goals\n9. Exit")

        # Read the user's selection
        option = input("Enter your option: ")

        # Option 1 — Add a new expense
        if option == "1":
            # Prompt for each field and validate; repeat until valid input
            while True:
                user_id = input("Enter your user ID: ")
                user_id = validation.validate_user_id(user_id)
                if user_id is not None:
                    break
                print("This field can not be empty!")

            while True:
                user_name = input("Enter your user name: ")
                user_name = validation.validate_user_name(user_name)
                if user_name is not None:
                    break
                print("This field can not be empty!")

            while True:
                spending_category = input("Enter the spending category: ")
                spending_category = validation.validate_spending_category(spending_category)
                if spending_category is not None:
                    break
                print("This field can not be empty!")

            while True:
                amount = input("Enter amount: ")
                amount = validation.validate_amount(amount)
                if amount is not None:
                    break
                print("Amount must be a valid number!")

            while True:
                date = input("Enter the date of the transaction in this format (dd/mm/yyyy): ")
                date = validation.validate_date(date)
                if date is not None:
                    break
                print("Field can not be empty and must have a valid date(dd/mm/yyyy)!")

            while True:
                description = input("Enter your description: ")
                description = validation.validate_description(description)
                if description is not None:
                    break
                print("This field can not be empty!")

            # Add the new expense using the processing module (pure logic)
            transactions = processing.add_an_expense(transactions, user_id, user_name, spending_category, amount, date, description)

            # Persist the updated transactions back to storage
            data["transactions"] = transactions
            data_store.save_data(data)

            print("Expense added successfully!")

        # Option 2 — View all expenses
        elif option == "2":

            if transactions:
                print("\n===== ALL EXPENSES =====")
                # Print each transaction (relies on transaction __str__/repr__)
                for transaction in transactions:
                    print(transaction)
            else:
                print("No expenses found!")

        # Option 3 — Update an expense
        elif option == "3":
            # Collect identifying criteria for the transaction(s) to update
            while True:
                user_id = input("Enter your user ID: ")
                user_id = validation.validate_user_id(user_id)
                if user_id is not None:
                    break
                print("This field can not be empty!")

            while True:
                spending_category = input("Enter the spending category: ")
                spending_category = validation.validate_spending_category(spending_category)
                if spending_category is not None:
                    break
                print("This field can not be empty!")

            while True:
                amount = input("Enter amount: ")
                amount = validation.validate_amount(amount)
                if amount is not None:
                    break
                print("Amount must be a valid number!")

            # Find matching transactions
            results = processing.find_transaction(transactions, user_id, spending_category, amount)

            if not results:
                print("Transaction not found!")
            else:
                # Show found transactions and ask which field to update
                for transaction in results:
                    print(transaction)
                print("1. Update user ID")
                print("2. Update user name")
                print("3. Update spending category")
                print("4. Update amount")
                print("5. Update date")
                print("6. Update description")
                field = input("Enter the field you want to update: ")

                # Based on selected field, prompt for the new value and validate it
                if field == "1":
                    while True:
                        modify = input("Enter new user ID: ")
                        modify = validation.validate_user_id(modify)
                        if modify is not None:
                            break
                        print("This field can not be empty!")
                elif field == "2":
                    while True:
                        modify = input("Enter your user name: ")
                        modify = validation.validate_user_name(modify)
                        if modify is not None:
                            break
                        print("This field can not be empty!")
                elif field == "3":
                    while True:
                        modify = input("Enter the spending category: ")
                        modify = validation.validate_spending_category(modify)
                        if modify is not None:
                            break
                        print("This field can not be empty!")
                elif field == "4":
                    while True:
                        modify = input("Enter amount: ")
                        modify = validation.validate_amount(modify)
                        if modify is not None:
                            break
                        print("Amount must be a valid number!")
                elif field == "5":
                    while True:
                        modify = input("Enter the date of the transaction in this format (dd/mm/yyyy): ")
                        modify = validation.validate_date(modify)
                        if modify is not None:
                            break
                        print("Field can not be empty and must have a valid date(dd/mm/yyyy)!")
                elif field == "6":
                    while True:
                        modify = input("Enter your description: ")
                        modify = validation.validate_description(modify)
                        if modify is not None:
                            break
                        print("This field can not be empty!")
                else:
                    # Invalid selection — do not attempt an update
                    print("Invalid field!")
                    modify = None

                # If a valid new value was gathered, perform the update and save
                if modify is not None:
                    transactions = processing.update_an_expense(
                        transactions,
                        user_id,
                        spending_category,
                        amount,
                        field,
                        modify
                    )

                    data["transactions"] = transactions
                    data_store.save_data(data)
                    print("Expense updated successfully!")

        # Option 4 — Delete an expense
        elif option == "4":
            # Get transaction identifier from the user (user_id, category, amount)
            while True:
                user_id = input("Enter your user ID: ")
                user_id = validation.validate_user_id(user_id)
                if user_id is not None:
                    break
                print("This field can not be empty!")

            while True:
                spending_category = input("Enter the spending category: ")
                spending_category = validation.validate_spending_category(
                    spending_category
                )
                if spending_category is not None:
                    break
                print("This field can not be empty!")

            while True:
                amount = input("Enter amount: ")
                amount = validation.validate_amount(amount)
                if amount is not None:
                    break
                print("Amount must be a valid number!")

            # Look up matching transactions
            results = processing.find_transaction(transactions, user_id, spending_category, amount)

            if not results:
                print("Transaction not found!")
            else:
                # Show found transactions, delete them, and save
                for transaction in results:
                    print(transaction)
                transactions = processing.delete_an_expense(transactions, user_id, spending_category, amount)
                data["transactions"] = transactions
                data_store.save_data(data)

                print("Expense deleted successfully!")

        # Option 5 — Search expenses by user ID
        elif option == "5":
            while True:
                user_id = input("Enter your user ID: ")
                user_id = validation.validate_user_id(user_id)
                if user_id is not None:
                    break
                print("This field can not be empty!")
            results = processing.search_expenses(transactions, user_id)
            if results:
                print("\n===== EXPENSES FOUND =====")
                for transaction in results:
                    print(transaction)
            else:
                print("No expenses found for this user!")

        # Option 6 — Calculate and display total expenses
        elif option == "6":

            total = processing.calculate_total_expenses(transactions)

            print("Total expenses: {:.2f}".format(total))

        # Option 7 — Show totals grouped by category
        elif option == "7":

            categories = processing.expenses_by_category(transactions)

            if categories:
                print("\n===== EXPENSES BY CATEGORY =====")

                # categories is expected to be a mapping: {category: total_amount}
                for category, total in categories.items():
                    print("{}: {:.2f}".format(category, total))
            else:
                print("No expenses found!")
        
        elif option == "8":
        #Option 8 : Provides an inteface for the  user to track their saving goals and display the saving progress
          while True:
  
              print("\n===== SAVING GOALS =====")
              print("1. Add saving goal")
              print("2. View saving goals")
              print("3. Update saving goal")
              print("4. Delete saving goal")
              print("5. Show saving progress")
              print("6. Back to main menu")
  
              goal_option = input("Enter your option: ")
  
              if goal_option == "1":
  
                  while True:
                      user_id = input("Enter your user ID: ")
                      user_id = validation.validate_user_id(user_id)
  
                      if user_id is not None:
                          break
  
                      print("This field cannot be empty!")
  
                  while True:
                      goal = input("Enter your saving goal: ")
                      goal = validation.validate_goal(goal)
  
                      if goal is not None:
                          break
  
                      print("This field cannot be empty!")
  
                  while True:
                      target_amount = input("Enter target amount: ")
                      target_amount = validation.validate_target_amount(target_amount)
  
                      if target_amount is not None:
                          break
  
                      print("Target amount must be greater than 0!")
  
                  while True:
                      saved_amount = input("Enter amount already saved: ")
                      saved_amount = validation.validate_amount(saved_amount)
  
                      if saved_amount is not None:
                          if saved_amount <= target_amount:
                              break
  
                      print("Invalid saved amount!")
  
                  while True:
                      deadline = input("Enter deadline (dd/mm/yyyy): ")
                      deadline = validation.validate_date(deadline)
  
                      if deadline is not None:
                          break
  
                      print("Invalid date!")
  
                  saving_goals = processing.add_saving_goal(
                      saving_goals,
                      user_id,
                      goal,
                      target_amount,
                      saved_amount,
                      deadline
                  )
  
                  data["saving_goals"] = saving_goals
                  data_store.save_data(data)
  
                  print("Saving goal added successfully!")
              elif goal_option == "2":
  
                  if saving_goals:
                      print("\n===== SAVING GOALS =====")
  
                      for saving_goal in saving_goals:
                          print(saving_goal)
                  else:
                      print("No saving goals found!")
  
              elif goal_option == "3":
  
                  while True:
                      user_id = input("Enter your user ID: ")
                      user_id = validation.validate_user_id(user_id)
  
                      if user_id is not None:
                          break
  
                      print("This field cannot be empty!")
                  goal = input("Enter the goal name: ")
  
                  results = processing.find_saving_goal(saving_goals, user_id, goal)
  
                  if not results:
                      print("Saving goal not found!")
  
                  else:
                      for saving_goal in results:
                          print(saving_goal)
  
                      print("1. Update goal")
                      print("2. Update target amount")
                      print("3. Update saved amount")
                      print("4. Update deadline")
  
                      field = input("Enter the field you want to update: ")
  
                      if field == "1":
                          modify = input("Enter the new goal: ")
                          modify = validation.validate_goal(modify)
  
                      elif field == "2":
                           while True:
                              modify = input("Enter the new target amount: ")
                              modify = validation.validate_target_amount(modify)
  
                              if modify is not None:
                                  current_saved = results[0]["saved_amount"]
  
                                  if modify >= current_saved:
                                      break
  
                              print("Target amount cannot be less than the amount already saved!")
  
  
                      elif field == "3":
                          while True:
                              modify = input("Enter the new saved amount: ")
                              modify = validation.validate_amount(modify)
  
                              if modify is not None:
                                  current_target = results[0]["target_amount"]
  
                                  if modify <= current_target:
                                      break
  
                              print("Saved amount cannot be greater than the target amount!")
  
                      elif field == "4":
                          modify = input("Enter the new deadline: ")
                          modify = validation.validate_date(modify)
  
                      else:
                          print("Invalid field!")
                          modify = None
  
                      if modify is not None:
                          saving_goals = processing.update_saving_goal(saving_goals, user_id, goal, field, modify)
  
                          data["saving_goals"] = saving_goals
                          data_store.save_data(data)
  
                          print("Saving goal updated successfully!")
  
  
              elif goal_option == "4":
  
                  while True:
                      user_id = input("Enter your user ID: ")
                      user_id = validation.validate_user_id(user_id)
  
                      if user_id is not None:
                          break
  
                      print("This field cannot be empty!")
                  goal = input("Enter the goal name: ")
  
                  results = processing.find_saving_goal(saving_goals, user_id, goal)
  
                  if not results:
                      print("Saving goal not found!")
  
                  else:
                      for saving_goal in results:
                          print(saving_goal)
  
                      saving_goals = processing.delete_saving_goal(saving_goals, user_id, goal)
  
                      data["saving_goals"] = saving_goals
                      data_store.save_data(data)
  
                      print("Saving goal deleted successfully!")
  
  
              elif goal_option == "5":
  
                  if not saving_goals:
                      print("No saving goals found!")
  
                  else:
                      progress = processing.calculate_saving_progress(
                          saving_goals
                      )
  
                      print("\n===== SAVING PROGRESS =====")
  
                      for result in progress:
                          print("Goal: {}".format(result["goal"]))
                          print("Progress: {:.2f}%".format(result["progress"]))
  
                          if result["progress"] >= 100:
                              print("Goal completed!")
  
                          print("-" * 30)
  
  
              elif goal_option == "6":
                      break
              else:
                  print("Invalid option!")
        elif option == "9":
            break
        else:
            print("Invalid input!")


if __name__ == "__main__":
    main()
