#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even(n):
    '''display “n is a number” only if n is an integer'''
    return render_template('6-number_odd_or_even.html', n=n)


app.run('0.0.0.0')
