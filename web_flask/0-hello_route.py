#!/usr/bin/python3
""" This defines flask"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def display():
	return "Hello HBNB!"

if __name__ == '__main_':
	app.run(host='0.0.0.0', port=5000)
