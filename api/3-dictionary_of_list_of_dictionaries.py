#!/usr/bin/python3
"""Gather data from an API"""
import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        exit()
    new_list = []
    new_dict = {}

    url = "https://jsonplaceholder.typicode.com"
    username = requests.get(f"{url}/users/{argv[1]}").json().get("username")
    total_list = requests.get(f"{url}/todos?userId={argv[1]}").json()
    sum_of_list = len(total_list)

    for todo in total_list:
        new_list.append({'username': username,
                         'task': todo.get('task'),
                         'completed': todo.get('completed')})
    new_dict[username.get("userId")] = new_list
    json.dump(new_dict, open(f"todo_all_employees.json", "w"))
