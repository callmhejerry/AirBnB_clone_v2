#!/usr/bin/python3
'''
Write a script that starts a Flask web application
'''
from flask import Flask

app = Flask(__name__)


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    '''display “n is a number” only if n is an integer'''
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
