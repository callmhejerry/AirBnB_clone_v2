#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    '''display HBNB'''
    return 'HBNB'


app.run('0.0.0.0')
