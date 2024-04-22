#!/usr/bin/python3

"""
This script fetches data from an API
and displays the employee's TODO list progress.
"""


import csv
import requests
import sys


def main(user_id):
    """
    Fetches employee data and TODO list from an API and displays the progress.
    """
    file_name = str(user_id) + ".csv"
    with open(file_name, mode='w') as csvfile:
        fieldnames = [
                "USER_ID",
                "USERNAME",
                "TASK_COMPLETED_STATUS",
                "TASK_TITLE"]
        writer = csv.DictWriter(
                csvfile,
                fieldnames=fieldnames,
                quoting=csv.QUOTE_ALL)

        url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
        response = requests.get(url)
        user_data = response.json()
        user_name = user_data["username"]

        response = requests.get(f'{url}/todos')
        user_todos = response.json()

        for user_todo in user_todos:
            writer.writerow({
                "USER_ID": user_todo["userId"],
                "USERNAME": user_name,
                "TASK_COMPLETED_STATUS": user_todo["completed"],
                "TASK_TITLE": user_todo["title"]})


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
