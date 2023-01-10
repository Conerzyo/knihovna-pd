import hashlib
from typing import Optional

from pymongo import MongoClient


class User:
    def __init__(self):
        self.id = None
        self.first_name = None
        self.last_name = None
        self.social_number = None
        self.address = None
        self.username = None
        self.hash = None
        self.loan_count = None
        self.active = None
        self.admin = None

    def create_dict(self):
        user_dict = {"firstName": self.first_name,
                     "lastName": self.last_name,
                     "socialNumber": self.social_number,
                     "address": self.address,
                     "username": self.username,
                     "hash": self.hash,
                     "loanCount": self.loan_count,
                     "active": self.active,
                     "admin": self.admin}
        return user_dict

    def fill_from_dict(self, dict_entry):
        if "_id" in dict_entry.keys():
            self.id = dict_entry["_id"]
        self.first_name = dict_entry["firstName"]
        self.last_name = dict_entry["lastName"]
        self.social_number = dict_entry["socialNumber"]
        self.address = dict_entry["address"]
        self.username = dict_entry["username"]
        self.hash = dict_entry["hash"]
        self.loan_count = dict_entry["loanCount"]
        self.active = dict_entry["active"]
        self.admin = dict_entry["admin"]


class Book:
    def __init__(self):
        self.id = None
        self.title = None
        self.author = None
        self.year = None
        self.pages = None
        self.count_overall = None
        self.count_available = None
        self.cover_photo = None


    def create_dict(self):
        user_dict = {"title": self.title,
                     "author": self.author,
                     "year": self.year,
                     "pages": self.pages,
                     "countOverall": self.count_overall,
                     "countAvailable": self.count_available,
                     "coverPhoto": self.cover_photo}
        return user_dict


    def fill_from_dict(self, dict_entry):
        if "_id" in dict_entry.keys():
            self.id = dict_entry["_id"]
        self.title = dict_entry["title"]
        self.author = dict_entry["author"]
        self.year = dict_entry["year"]
        self.pages = dict_entry["pages"]
        self.count_overall = dict_entry["countOverall"]
        self.count_available = dict_entry["countAvailable"]
        self.cover_photo = dict_entry["coverPhoto"]


class Loan:
    def __init__(self):
        self.book_id = None
        self.user_id = None
        self.loan_date = None
        self.due_date = None
        self.end_date = None

    def create_dict(self):
        user_dict = {"bookId": self.book_id,
                     "userId": self.user_id
                     }
        return user_dict


class DatabaseConnection:
    database_name = "AK7PD"
    books_collection_name = "books"
    users_collection_name = "users"
    loans_collection_name = "loans"
    book_cover_photo = "coverPhoto"

    def __init__(self, connection_string):
        self.client = MongoClient(connection_string)

    def login(self, username, hash) -> Optional[User]:
        user = self.__get_user({"username": username, "hash": hash})
        if user is None or not user.active:
            return None
        return user

    def create_book(self, book) -> bool:
        exists = self.client[self.database_name][self.books_collection_name].find_one({"title": book.title})
        if exists is not None:
            print(f"[ERROR] Book {book.title} already exists.")
            return False
        return self.client[self.database_name][self.books_collection_name].insert_one(book.create_dict()).acknowledged

    def create_user(self, user) -> bool:
        exists = self.client[self.database_name][self.users_collection_name].find_one({"username": user.username})
        if exists is not None:
            print(f"[ERROR] User {user.username} already exists.")
            return False
        return self.client[self.database_name][self.users_collection_name].insert_one(user.create_dict()).acknowledged

    def get_user_by_id(self, user_id) -> Optional[User]:
        return self.__get_user({"_id": user_id})

    def get_user_by_username(self, username) -> Optional[User]:
        return self.__get_user({"username": username})

    def __get_user(self, query) -> Optional[User]:
        user_dict = self.client[self.database_name][self.users_collection_name].find_one(query)
        if user_dict is None:
            return None
        user = User()
        user.fill_from_dict(user_dict)
        return user

    def get_book_by_title(self, title) -> Optional[Book]:
        return self.__get_book({"title": title})

    def get_book_by_id(self, book_id) -> Optional[Book]:
        return self.__get_book({"_id": book_id})

    def __get_book(self, query) -> Optional[Book]:
        book_dict = self.client[self.database_name][self.books_collection_name].find_one(query)
        if book_dict is None:
            return None
        book = Book()
        book.fill_from_dict(book_dict)
        return book

    def create_loan(self, loan) -> bool:
        book = self.get_book_by_id(loan.book_id)
        user = self.get_user_by_id(loan.user_id)

        if book is None:
            print(f"[ERROR] Book not found")
            return False
        if user is None:
            print(f"[ERROR] User not found")
            return False
        if book.count_available < 1:
            print(f"[ERROR] Not enough books")
            return False
        if not user.active:
            print(f"[ERROR] User {user.username} is not active")
            return False
        if user.loan_count >= 6:
            print(f"[ERROR] User {user.username} cannot loan more than 6 books")
            return False

        return self.client[self.database_name][self.loans_collection_name].insert_one(loan.create_dict()).acknowledged

    def clear_databases(self):
        self.client[self.database_name][self.books_collection_name].delete_many({})
        self.client[self.database_name][self.users_collection_name].delete_many({})
        self.client[self.database_name][self.loans_collection_name].delete_many({})