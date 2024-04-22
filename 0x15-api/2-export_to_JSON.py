#!/usr/bin/python3

"""
This script fetches data from an API
and displays the employee's TODO list progress.
"""


import json
import requests
import sys


def main(user_id):
    """
    Fetches employee data and TODO list from an API and displays the progress.
    """
    file_name = str(user_id) + ".json"
    with open(file_name, mode='w') as jsonfile:

        url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
        user_data = requests.get(url).json()
        user_name = user_data["username"]
        user_todos = requests.get(f'{url}/todos').json()

        json.dump({user_id: [{
            "task": user_todo.get("title"),
            "completed": user_todo.get("completed"),
            "username": user_name
        } for user_todo in user_todos]}, jsonfile)


if __name__ == "__main__":
    """
    Executes the main function
    with the provided employee ID as a command-line argument.
    """
    if len(sys.argv) < 2:
        print('Usage: python3 script.py <employee_id>')
        sys.exit(1)

    user_id = sys.argv[1]
    main(user_id)
