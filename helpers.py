import csv
import urllib.request

from cs50 import SQL

from flask import redirect, render_template, request, session
from functools import wraps

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///foodiematch.db")


def apology(message, code=400):
    """Renders message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def check_matches(user_id):
    """returns list of all matches for the given id"""
    matchlist = []
    matches = db.execute("SELECT likedid FROM like WHERE currentid=:id", id=user_id)
    matches = [int(id) for id in str(matches) if id.isdigit()]
    for id in matches:
        match2 = db.execute("SELECT likedid FROM like WHERE currentid=:id", id=id)
        match2 = [int(id) for id in str(match2) if id.isdigit()]
        if user_id in match2:
            matchlist.append(id)
    return set(matchlist)


