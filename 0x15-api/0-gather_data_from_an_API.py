#!/usr/bin/python3

"""
This script fetches data from an API
and displays the employee's TODO list progress.
"""


import requests
import sys


def main(user_id):
    """
    Fetches employee data and TODO list from an API and displays the progress.
    """
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    response = requests.get(url)
    user_data = response.json()
    user_name = user_data['name']

    response = requests.get(f'{url}/todos')
    user_todos = response.json()

    total_tasks = len(user_todos)
    completed_tasks = sum(user_todo['completed'] for user_todo in user_todos)

    progress_message = (
        f'Employee {user_name} is done with tasks'
        f'({completed_tasks}/{total_tasks}):'
    )
    print(progress_message)
    for user_todo in user_todos:
        if user_todo['completed']:
            print(f'\t {user_todo["title"]}')


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
