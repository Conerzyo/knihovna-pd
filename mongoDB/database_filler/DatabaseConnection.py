from pymongo import MongoClient


class DatabaseConnection:
    database_name = "AK7PD"
    books_collection_name = "books"
    users_collection_name = "users"
    loans_collection_name = "loans"
    book_cover_photo = "coverPhoto"

    def __init__(self, host, port, username, password):
        self.client = MongoClient(host=host, port=port, username=username, password=password, timeoutMs=2000)

    def drop_databases(self):
        self.client.drop_database(self.database_name)

    def add_book_structure(self, book):
        ret_value = self.client[self.database_name][self.books_collection_name].insert_one(book)

    def add_user_structure(self, user):
        ret_value = self.client[self.database_name][self.users_collection_name].insert_one(user)

    def add_loan_structure(self, loan):
        ret_value = self.client[self.database_name][self.loans_collection_name].insert_one(loan)
