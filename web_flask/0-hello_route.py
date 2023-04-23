#!/usr/bin/python3

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_page():
    '''return hello hbnb'''
    return "Hello HBNB!"

app.run('0.0.0.0', debug=True)
