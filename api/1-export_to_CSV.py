#!/usr/bin/python3
"""Gather data from an API"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        exit()

    url = "https://jsonplaceholder.typicode.com"
    username = requests.get(f"{url}/users/{argv[1]}").json().get("username")
    total_list = requests.get(f"{url}/todos?userId={argv[1]}").json()

    sum_of_list = len(total_list)



    writer = csv.writer(open(f"{argv[1]}.csv", "w"), quoting=csv.QUOTE_ALL)

    for i in total_list:
        writer.writerow([i.get("userId"), username, i.get("completed"),
                          i.get("title")])

