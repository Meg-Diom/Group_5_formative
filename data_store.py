#!/usr/bin/env python3
"""This module provides functions for loading and saving budget data in JSON format"""

import json

DEFAULT_JSON = {
            "transactions": [],
            "saving_goals": []
        }
def load_data():
    """
    load_data function loads budget from a JSON file and saves it as a dictionary
    If the file cannnot be found, read or contains invalid JSON syntax, the program 
    will return an empty data dictionary
    """

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Error: File not found!")
        return DEFAULT_JSON
    except json.JSONDecodeError:
        print("Error: Invalid JSON format")
        return DEFAULT_JSON
    
    except IOError:
        print("Error: Couldn't read this file!")
        return DEFAULT_JSON

    
def save_data(data):
    """save_data function saves data from a python dictionary to a JSON format.
    dictionary contains transactions by the user
    the data is saved with indentation so that it can easily be read"""

    try:
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
    except IOError:
        print("Error: Could not save file!")

