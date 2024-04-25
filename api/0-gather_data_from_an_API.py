#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    if argv == 2:
        exit()
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(f"{url}/users/{argv[1]}").json()
    total_list = requests.get(f"{url}/todos?userId={argv[1]}").json()

    sum_of_list = len(total_list)
    number_of_done_tasks = 0
    completed_task_name = ""

    for i in total_list:
        if i["completed"]:
            number_of_done_tasks += 1
            completed_task_name += "\t" + i.get("title") + "\n"

    print("Employee {} is done with tasks({}/{}):".
          format(user, number_of_done_tasks, total_list))
    print(completed_task_name)
