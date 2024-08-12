#!/usr/bin/python3
"""
A simple Flask web application that displays a list of states from a database.

Routes:
    /states_list: Displays an HTML page with a list of states from the database.

The application uses the Flask framework and SQLAlchemy for ORM.
It connects to a database to fetch state data and render it in a template.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def handle():
    """
    Handle the /states_list route.
    
    Retrieves all State objects from the database and renders them in an HTML template.
    The states are displayed in alphabetical order by name.

    Returns:
        str: Rendered HTML page with a list of states.
    """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown(exception):
    """
    Close the SQLAlchemy session after each request.

    Args:
        exception (Exception): Exception that was raised during the request, if any.
    """
    storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)