#!/usr/bin/env python3

import json

DEFAULT_JSON = {
            "transactions": [], 
            "saving_goals": []
        }
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

    
def save_data(data):

    try:
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
    except IOError:
        print("Error: Could not save file!")

