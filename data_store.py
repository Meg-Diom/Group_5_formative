#!/usr/bin/env python3
# Module for loading and saving budget data in JSON format

import json

DEFAULT_JSON = {
            "transactions": [],
            "saving_goals": []
        }

# Loads budget from JSON file, returns DEFAULT_JSON if file not found or invalid
def load_data():
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

    
# Saves data dictionary to JSON file with indentation for readability
def save_data(data):
    try:
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
    except IOError:
        print("Error: Could not save file!")
