import csv
import urllib.request

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for

import re
from sightengine.client import SightengineClient

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
    """returns set of all matches for the given id"""
    matchlist = []
    matches = db.execute("SELECT likedid FROM like WHERE currentid=:id", id=user_id)
    matches = [int(user) for user in re.findall('\d+', str(matches))]
    for id in matches:
        match2 = db.execute("SELECT likedid FROM like WHERE currentid=:id", id=id)
        match2 = [int(user) for user in re.findall('\d+', str(match2))]
        if user_id in match2 and id != user_id:
            matchlist.append(id)
    return set(matchlist)

def check_liked(user_id):
    """returns set of all likes given by the given id"""
    likelist = []
    matches = db.execute("SELECT likedid FROM like WHERE currentid=:id", id=user_id)
    matches = [int(user) for user in re.findall('\d+', str(matches))]
    for id in matches:
        if id != user_id:
            likelist.append(id)
    return set(likelist)

def imagereport(imageid):
    """returns report on image"""
    client = SightengineClient('80581480', 'ishfWhtrSrVWnnYEUYWj')
    output = client.check('nudity','wad','offensive','faces').set_file(imageid)
    return output

def imagecheck(report):
    """returns whether or not image content is approved"""
    if report['status'] == 'failure':
        print("status")
        return "File is not approved"
    if report['weapon'] >= 0.85:
        print("weapon")
        return "Image shows weapons"
    if report['drugs'] >= 0.85:
        print("drugs")
        return "image shows drugs"
    if report['nudity']['raw'] >= 0.85 or report['nudity']['partial'] >= 0.85:
        print("nudity")
        return "Image shows nudity"
    if report['faces'] != []:
        print("faces")
        return "Image not approved"
    if report['offensive']['prob'] >= 0.85:
        print("offensive")
        return "Image shows offensive content"
    return True

