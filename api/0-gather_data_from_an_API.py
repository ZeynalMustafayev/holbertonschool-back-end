#!usr/bin/python3
from flask import Flask
from flask import request
import json

app = Flask("__name__")

@app.route("/")
def response():
    response = request.get("https://jsonplaceholder.typicode.com/todos")

    print(response)

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")