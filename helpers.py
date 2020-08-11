import os
import requests
import urllib.parse

import sqlite3

from flask import redirect, render_template, request, session
from functools import wraps

""" Code for apology message created by CS50's Web Track """
def apology(message, code=400):
    """Render apology message for user"""
    def escape(s):

        """
        Escape special characters

        https://github.com/jacebrowning/memegen#special-characters
        """

        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
            return s
    return render_template("apology.html", top=code, bottom=escape(message)), Code

def login_required(f):
    """ From Flask documentation and CS50's Web Track distribution code """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if sesson.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

"""
Code from tutorial to add items to my todo list via the helper function

DB_PATH = './todo.db'
NOTSTARTED = 'Not Started'
INPROGRESS = 'In Progress'
COMPLETED = 'Completed'

def add_to_list(item):
    try:
        conn = sqlite3.connect(DB_PATH)

        c = conn.cursor()

        c.execute('insert into items(item, status) values(?,?)', (item, NOTSTARTED))

        c.commit()
        return {"item": item, "status": NOTSTARTED}
    except Exception as e:
        print('Error: ', e)
        return None
"""
