import hashlib
import os
from dotenv import load_dotenv
from pathlib import Path

from flask import Flask, request
from flask_restful import Api, Resource


from DatabaseConnection import DatabaseConnection, User, Loan, Book
from MongoFiller import MongoFiller

from User import UserAPI
from Loan import LoanAPI
from Book import BookAPI
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


def password_hash(password):
    hasher = hashlib.md5()
    hasher.update(password.encode('utf-8'))
    return hasher.hexdigest()


@app.route("/login", methods=["POST"])
def login():
    auth.login()

    username = request.form.get("username")
    password = password_hash(request.form.get("password"))

    return userApi.login(username, password)


@app.route("/logout", methods=["GET"])
def logout():
    auth.logout()
    return {}
# ---------------------------------------------------------------- ADMIN


@app.route("/admin/importDb", methods=["POST"])
def admin_importDb():
    inputfile = open("export.json", 'w')
    filler = MongoFiller(database_connection=DatabaseConnection(connection_string=connection_str), data_file=inputfile)
    filler.import_json()
    return {}


@app.route("/admin/exportDb", methods=["GET"])
def admin_exportDb():
    outfile = open("export.json", 'w')
    filler = MongoFiller(database_connection=DatabaseConnection(connection_string=connection_str), data_file=outfile)
    json_string = filler.get_export_data()


    return json_string


@app.route("/admin/activateUser", methods=["GET"])
def admin_activateUser():
    return userApi.activateUser(request.args.get("userId"))
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

    return {}


@app.route("/users/editUser", methods=["POST"])
def users_editUser():
    user = User()
    userId = request.form.get("userId")

    user.first_name = request.form.get("firstName")
    user.last_name = request.form.get("lastName")
    user.social_number = request.form.get("socialNumber")
    user.address = request.form.get("address")
    user.hash = password_hash(request.form.get("password"))

    userApi.edit(userId=userId, user=user)
    return {}

@app.route("/users/getByName", methods=["GET"])
def users_getByName():
    return userApi.getByName(request.args.get("name"))


@app.route("/users/getById", methods=["GET"])
def users_getById():
    return userApi.getById(request.args.get("id"))


@app.route("/users/getAll", methods=["GET"])
def users_getAll():
    return userApi.getAllUsers()


@app.route("/users/findUsers", methods=["GET"])
def users_findUsers():
    first_name = request.args.get("firstName")
    last_name = request.args.get("lastName")
    address = request.args.get("address")
    social_number = request.args.get("socialNumber")
    sort_by = request.args.get("sortBy")

    return userApi.findUsers(first_name=first_name,
                             last_name=last_name,
                             address=address,
                             social_number=social_number,
                             sort_by=sort_by)
# ---------------------------------------------------------------- BOOK


@app.route("/books/create", methods=["POST"])
def books_create():
    book = Book()
    book.title = request.form.get("title")
    book.author = request.form.get("author")
    book.year = request.form.get("year")
    book.pages = request.form.get("pages")
    book.count_overall = request.form.get("countOverall")
    book.count_available = request.form.get("countAvailable")
    book.cover_photo = request.form.get("coverPhoto")


@app.route("/books/getByTitle", methods=["GET"])
def books_getByTitle():
    return bookApi.getByTitle(request.args.get("title"))


@app.route("/books/getById", methods=["GET"])
def books_getById():
    return bookApi.getById(request.args.get("id"))


@app.route("/books/getAll", methods=["GET"])
def books_getAll():
    return bookApi.getAllBooks()


@app.route("/books/uploadPicture", methods=["GET"])
def books_getUploadPicture():
    return {}


@app.route("/books/findBooks", methods=["GET"])
def books_findBooks():
    title = request.args.get("title")
    year = request.args.get("year")
    author = request.args.get("author")

    return bookApi.findBook(title=title, year=year, author=author)
# ---------------------------------------------------------------- LOAN


@app.route("/loans/create", methods=["POST"])
def loans_create():
    loan = Loan()
    loan.user_id = request.form.get("userId")
    loan.book_id = request.form.get("bookId")


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
