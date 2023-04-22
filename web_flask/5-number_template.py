#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''display “n is a number” only if n is an integer'''
    return render_template('5-number.html', n=n)

app.run('0.0.0.0')
