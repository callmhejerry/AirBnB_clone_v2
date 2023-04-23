#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_route(text='is cool'):
    '''displays Python followed by [text]'''
    new_text = text.replace('_', ' ')
    return 'Python {}'.format(new_text)


app.run('0.0.0.0')
