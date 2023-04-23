#!/usr/bin/python3
'''
Write a script that starts a Flask web application
'''
from flask import Flask

app = Flask(__name__)


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    new_text = text.replace('_', ' ')
    return "C {}".format(new_text)


app.run('0.0.0.0')
