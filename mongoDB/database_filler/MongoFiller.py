import base64
import hashlib
import json
import os

from DatabaseConnection import User, Book, Loan
from bson import json_util

class MongoFiller:
    books_entry_name = "books"
    users_entry_name = "users"
    loans_entry_name = "loans"

    def __init__(self, database_connection, data_file):
        self.database_connection = database_connection

    #import from simple json
    def __import_json_old(self, to_import):
        self.database_connection.clear_databases()
        self.__insert_books_from_json()
        self.__create_users_from_json()
        self.__create_loans_from_json()

    #import from mongo json, this works with the exported data
    def import_json(self, to_import):
        self.database_connection.clear_databases()
        self.data = to_import
        for book in self.data[self.books_entry_name]:
            book_dict = json_util.loads(book)
            book = Book()
            book.fill_from_dict(book_dict)
            self.database_connection.create_book(book)

        for user in self.data[self.users_entry_name]:
            user_dict = json_util.loads(user)
            user = User()
            user.fill_from_dict(user_dict)
            self.database_connection.create_user(user)

        for loan in self.data[self.loans_entry_name]:
            loan_dict = json_util.loads(loan)
            loan = Loan()
            loan.fill_from_dict(loan_dict)
            self.database_connection.create_loan(loan)

    def get_export_data(self):
        output = {}
        books = self.database_connection.get_all_books()
        loans = self.database_connection.get_all_loans()
        users = self.database_connection.get_all_users()

        output[self.books_entry_name] = []
        output[self.users_entry_name] = []
        output[self.loans_entry_name] = []

        for book in books:
            book_dict = book.create_dict()
            output[self.books_entry_name].append(json_util.dumps(book_dict))
        for user in users:
            output[self.users_entry_name].append(json_util.dumps(user.create_dict()))
        for loan in loans:
            output[self.loans_entry_name].append(json_util.dumps(loan.create_dict()))
        return json.dumps(output)

    def __insert_books_from_json(self):
        for book_entry in self.data[self.books_entry_name]:
            book = Book()
            cover_photo_path = self.data_json_folder + "/" + book_entry["coverPhoto"]
            with open(cover_photo_path, 'rb') as f:
                cover_photo = f.read()

            book_entry["coverPhoto"] = cover_photo
            book_entry["countAvailable"] = book_entry["countOverall"]
            book.fill_from_dict(book_entry)
            self.database_connection.create_book(book)

    def __create_users_from_json(self):
        for user_entry in self.data[self.users_entry_name]:
            user_entry["hash"] = self.__password_hash(user_entry["password"])
            user_entry["loanCount"] = 0
            user = User()
            user.fill_from_dict(user_entry)
            self.database_connection.create_user(user)

    def __create_loans_from_json(self):
        for loan_entry in self.data[self.loans_entry_name]:
            loan = Loan()
            loan.user_id = self.database_connection.get_user_by_username(loan_entry["username"]).id
            loan.book_id = self.database_connection.get_book_by_title(loan_entry["title"]).id
            self.database_connection.create_loan(loan)

    def __password_hash(self, password):
        hasher = hashlib.md5()
        hasher.update(password.encode('utf-8'))
        return hasher.hexdigest()

