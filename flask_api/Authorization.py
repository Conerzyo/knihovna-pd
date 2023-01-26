from DatabaseConnection import User
from flask import Flask, request, session


def login(self, user):
    if request.method == "POST":
        session.permanent = True
        session["user"] = str(user.id)
        session["isAdmin"] = user.admin
        return True
    else:
        if "user" in session:
            return True

        return False


def logout():
    session.pop("user", None)
    session.pop("isAdmin", None)
    return True


def isLoggedIn():
    if "user" in session:
        return session["user"]
    else:
        return False


def isAdmin():
    if isLoggedIn() and ("isAdmin" in session):
        return session["isAdmin"]
    else:
        return False
