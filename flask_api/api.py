import hashlib
import os
from dotenv import load_dotenv
from pathlib import Path

from flask import Flask, request
from flask_restful import Api, Resource


from mongoDB.database_filler.DatabaseConnection import User, Loan, Book

from User import UserAPI
from Loan import LoanAPI
from Book import BookAPI
from Admin import AdminAPI
import Authorization

dotenv_path = Path('connection_string.env')
load_dotenv(dotenv_path=dotenv_path)

app = Flask(__name__)
app.secret_key = "test key"
api = Api(app)
auth = Authorization

connection_str = os.getenv("connection_string")

userApi = UserAPI(connection_string=connection_str)
loanApi = LoanAPI(connection_string=connection_str)
bookApi = BookAPI(connection_string=connection_str)
adminApi = AdminAPI(connection_string=connection_str)


@app.route("/login", methods=["POST"])
def login():
    return auth.login()


@app.route("/logout", methods=["POST"])
def logout():
    return auth.logout()
# ---------------------------------------------------------------- ADMIN


@app.route("/admin/importDb", methods=["POST"])
def admin_importDb():
    return {}


@app.route("/admin/exportDb", methods=["POST"])
def admin_exportDb():
    return {}


@app.route("/admin/activateUser", methods=["POST"])
def admin_activateUser():
    return {}


@app.route("/admin/editUser", methods=["POST"])
def admin_editUser():
    return {}
# ---------------------------------------------------------------- USER


@app.route("/users/create", methods=["POST"])
def users_create():
    user = User()
    user.username = request.args.get("username")
    user.hash = hashlib.sha256(request.args.get("password").encode())
    user.first_name = request.args.get("firstName")
    user.last_name = request.args.get("lastName")
    user.social_number = request.args.get("socialNumber")
    user.address = request.args.get("address")
    userApi.create(request.args.get("name"))


@app.route("/users/getByName", methods=["GET"])
def users_getByName():
    return userApi.getByName(request.args.get("name"))


@app.route("/users/getById", methods=["GET"])
def users_getById():
    return userApi.getById(request.args.get("id"))


@app.route("/users/getAll", methods=["GET"])
def users_getAll():
    return userApi.getAllUsers()
# ---------------------------------------------------------------- BOOK


@app.route("/books/create", methods=["POST"])
def books_create():
    book = Book()
    book.title = request.args.get("title")
    book.author = request.args.get("author")
    book.year = request.args.get("year")
    book.pages = request.args.get("pages")
    book.count_overall = request.args.get("countOverall")
    book.count_available = request.args.get("countAvailable")
    book.cover_photo = request.args.get("coverPhoto")


@app.route("/books/getByName", methods=["POST"])
def books_getByName():
    return bookApi.getByName(request.args.get("name"))


@app.route("/books/getById", methods=["POST"])
def books_getById():
    return bookApi.getById(request.args.get("id"))


@app.route("/books/getAll", methods=["POST"])
def books_getAll():
    return bookApi.getAllBooks()
# ---------------------------------------------------------------- LOAN


@app.route("/loans/create", methods=["POST"])
def loans_create():
    loan = Loan()
    loan.title = request.args.get("title")
    loan.author = request.args.get("author")


@app.route("/loans/getByName", methods=["POST"])
def loans_getByName():
    return loanApi.getByName(request.args.get("name"))


@app.route("/loans/getById", methods=["POST"])
def loans_getById():
    return loanApi.getById(request.args.get("id"))


@app.route("/loans/getAll", methods=["POST"])
def loans_getAll():
    return loanApi.getAllBooks()


if __name__ == "__main__":
    app.run(debug=True)
