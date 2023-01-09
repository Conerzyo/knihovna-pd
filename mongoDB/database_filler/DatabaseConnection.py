from pymongo import MongoClient
import time

class DatabaseConnection:
    database_name = "AK7PD"
    books_collection_name = "books"
    users_collection_name = "users"
    loans_collection_name = "loans"
    book_cover_photo = "coverPhoto"

    def __init__(self, connection_string):
        self.client = MongoClient(connection_string)

    def drop_databases(self):
        self.client[self.database_name][self.books_collection_name].delete_many({})
        self.client[self.database_name][self.users_collection_name].delete_many({})
        self.client[self.database_name][self.loans_collection_name].delete_many({})
        return

    def add_book_structure(self, book):
        ret_value = self.client[self.database_name][self.books_collection_name].insert_one(book)
        return

    def add_user_structure(self, user):
        ret_value = self.client[self.database_name][self.users_collection_name].insert_one(user)
        return

    def add_loan_structure(self, loan):
        book = loan["title"]
        user = loan["username"]
        self.add_loan(book, user)
        #entry = {"book": book, "user": user}
        #ret_value = self.client[self.database_name][self.loans_collection_name].insert_one(entry)
        #todo validation insert https://stackoverflow.com/questions/46569262/does-pymongo-have-validation-rules-built-in

    def add_loan(self, title, user_name):
        book = self.client[self.database_name][self.books_collection_name].find_one({"title": title})
        user = self.client[self.database_name][self.users_collection_name].find_one({"username": user_name})

        #todo check in triger?
        if book is None:
            print(f"[ERROR] Book {title} not found")
            return False
        if user is None:
            print(f"[ERROR] User {user_name} not found")
            return False
        if book['countAvailable'] < 0 or not user['active']:
            print(f"[ERROR] Not enough books {title}")
            return False
        if not user['active']:
            print(f"[ERROR] User {user_name} is not active")
            return False
        if user['loanCount'] >= 6:
            print(f"[ERROR] User {user_name} cannot loan more than 6 books")
            return False

        entry = {"book": book['_id'], "user": user['_id']} #todo get rid of constants, create model
        ret_value = self.client[self.database_name][self.loans_collection_name].insert_one(entry)
        return True

    def create_triggers(self):
        return
