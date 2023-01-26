from mongoDB.database_filler.DatabaseConnection import DatabaseConnection, User
from flask import Flask, request, session


def login():
    if request.method == "POST":
        session.permanent = True
        session["user"] = "TEST USER"
        return True
    else:
        if "user" in session:
            return True

        return False


def logout():
    session.pop("user", None)
    return True


def isLoggedIn():
    if "user" in session:
        return True
    else:
        return False


def isAdmin():
    if isLoggedIn() and ("isAdmin" in session):
        return True
    else:
        return False
