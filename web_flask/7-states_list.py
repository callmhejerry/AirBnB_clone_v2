#!/usr/bin/python3
""" Starts a Flask application related to HBNB. """

if __name__ == "__main__":
    from flask import Flask, render_template
    from models import storage
    from models.state import State

    app = Flask(__name__)

    @app.teardown_appcontext
    def tear_down(exception):
        """removes the current SQLAlchemy session"""
        storage.close()

    @app.route('/states_list', strict_slashes=False)
    def states_list():
        """Displays a list of states"""
        all_states = storage.all(State).values()
        return render_template('7-states_list.html', states=all_states)

    app.run('0.0.0.0', port=5000)
