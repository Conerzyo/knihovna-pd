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


def password_hash(password):
    hasher = hashlib.md5()
    hasher.update(password)
    return hasher.hexdigest()


@app.route("/login", methods=["POST"])
def login():
    return auth.login()


@app.route("/logout", methods=["GET"])
def logout():
    return auth.logout()
# ---------------------------------------------------------------- ADMIN


@app.route("/admin/importDb", methods=["POST"])
def admin_importDb():
    return {}


@app.route("/admin/exportDb", methods=["POST"])
def admin_exportDb():
    return {}


@app.route("/admin/activateUser", methods=["GET"])
def admin_activateUser():
    return {}
# ---------------------------------------------------------------- USER


@app.route("/users/create", methods=["POST"])
def users_create():
    user = User()
    user.username = request.form.get("username")
    user.first_name = request.form.get("firstName")
    user.last_name = request.form.get("lastName")
    user.social_number = request.form.get("socialNumber")
    user.address = request.form.get("address")
    user.hash = password_hash(request.form.get("password"))
    userApi.create(user)


@app.route("/users/editUser", methods=["POST"])
def users_editUser():
    user = User()
    user.username = request.args.get("username")
    user.hash = hashlib.md5(request.args.get("password").encode())
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


@app.route("/users/findUser", methods=["GET"])
def users_findUser():
    first_name = request.args.get("firstName")
    last_name = request.args.get("lastName")
    address = request.args.get("address")
    social_number = request.args.get("socialNumber")
    sort_by = request.args.get("sortBy")

    return userApi.findUser(first_name=first_name, last_name=last_name, address=address, social_number=social_number)
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


@app.route("/books/getByTitle", methods=["GET"])
def books_getByTitle():
    return bookApi.getByTitle(request.args.get("title"))


@app.route("/books/getById", methods=["GET"])
def books_getById():
    return bookApi.getById(request.args.get("id"))


@app.route("/books/getAll", methods=["GET"])
def books_getAll():
    return bookApi.getAllBooks()

@app.route("/books/findBook", methods=["GET"])
def books_findBooks():
    title = request.args.get("title")
    year = request.args.get("year")
    author = request.args.get("author")

    return bookApi.findBook(title=title, year=year, author=author)
# ---------------------------------------------------------------- LOAN


@app.route("/loans/create", methods=["POST"])
def loans_create():
    loan = Loan()
    loan.user_id = request.args.get("userId")
    loan.book_id = request.args.get("bookId")


@app.route("/loans/getByUserId", methods=["GET"])
def loans_getByUserId():
    return loanApi.getByUserId(request.args.get("id"))


@app.route("/loans/getActiveLoans", methods=["GET"])
def loans_getActiveLoans():
    return loanApi.getActiveLoans(request.args.get("id"))


@app.route("/loans/getAll", methods=["GET"])
def loans_getAll():
    return loanApi.getAllLoans()


if __name__ == "__main__":
    app.run(debug=True)
