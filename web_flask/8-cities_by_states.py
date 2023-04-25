#!/usr/bin/python3
'''
A script that starts a Flask web application
'''


if __name__ == "__main__":
    from os import getenv
    from flask import Flask, render_template
    from models import storage
    from models.state import State

    app = Flask(__name__)

    @app.route('/cities_by_states', strict_slashes=False)
    def cities_by_states():
        '''Displays the cities and states'''
        all_state = None
        if getenv("HBNB_TYPE_STORAGE") == "db":
            all_state = storage.all(State).values()
        else:
            all_state = storage.all(State).values()
        return render_template('8-cities_by_states.html', states=all_state)

    @app.teardown_appcontext
    def tear_down_app(exception):
        '''called after each request'''
        storage.close()

    app.run('0.0.0.0', debug=True)
