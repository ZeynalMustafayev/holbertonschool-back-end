#!/usr/bin/python3
import json
import requests
from sys import argv

if __name__ == "__main__":

    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{argv[1]}").json().get('name')
    total_list = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}").json()

    sum_of_list = len(total_list)
    number_of_done_tasks = 0
    completed_task_name = ""

    for i in total_list:
        if i["completed"]:
            number_of_done_tasks += 1
            completed_task_name += "\t" + i.get("title") + "\n"

    print(f"Employee {user} is done with tasks({number_of_done_tasks}/{sum_of_list})")
    print(completed_task_name)

    

