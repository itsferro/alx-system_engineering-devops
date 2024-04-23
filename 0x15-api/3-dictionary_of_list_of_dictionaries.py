#!/usr/bin/python3

"""
This script fetches data from an API
and displays the employee's TODO list progress.
"""


import json
import requests
import sys


def main():
    """
    Fetches employee data and TODO list from an API and displays the progress.
    """
    with open("todo_all_employees.json", mode='w') as jsonfile:

        url = f'https://jsonplaceholder.typicode.com/'
        users = requests.get(url + "users").json()

        json.dump({
            user.get("id"): [
                {
                    "username": user.get("username"),
                    "task": task.get("title"),
                    "completed": task.get("completed")
                } for task in requests.get(
                    url + "todos",
                    params={"userId": user.get("id")}).json()
                ]
            for user in users},
            jsonfile
        )


if __name__ == "__main__":
    main()
