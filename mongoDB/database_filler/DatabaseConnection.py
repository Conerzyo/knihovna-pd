from pymongo import MongoClient


class DatabaseConnection:
    database_name = "AK7PD"
    books_collection_name = "books"
    users_collection_name = "users"
    loans_collection_name = "loans"
    book_cover_photo = "coverPhoto"

    def __init__(self, connection_string):
        self.client = MongoClient(connection_string)

    def drop_databases(self):
        #self.client.drop_database(self.database_name)
        #self.client[self.database_name].drop_collection(self.books_collection_name)
        #self.client[self.database_name].drop_collection(self.users_collection_name)
        #self.client[self.database_name].drop_collection(self.loans_collection_name)
        return

    def add_book_structure(self, book):
        ret_value = self.client[self.database_name][self.books_collection_name].insert_one(book)

    def add_user_structure(self, user):
        ret_value = self.client[self.database_name][self.users_collection_name].insert_one(user)

    def add_loan_structure(self, loan):
        book = loan["book"]
        user = loan["user"]
        entry = {"book": book, "user": user}
        ret_value = self.client[self.database_name][self.loans_collection_name].insert_one(entry)

    def create_triggers(self):
        return
