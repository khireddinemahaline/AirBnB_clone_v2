#!/usr/bin/python3
"""return hello HBNB using flask"""

from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def handel_teardown():
    storage.close()

@app.route('/states_list')
def handel():
    states = storage.all(State).values()
    return render_template('7-states_list.html', states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
