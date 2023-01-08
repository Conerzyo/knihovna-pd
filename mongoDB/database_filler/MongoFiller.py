import json
import os


class MongoFiller:
    books_entry_name = "books"
    users_entry_name = "users"
    loans_entry_name = "loans"
    book_cover_photo = "coverPhoto"

    def __init__(self, database_connection, data_file):
        self.data_json_folder = os.path.dirname(data_file)
        with open(data_file, 'r') as f:
            self.data = json.load(f)
        self.database_connection = database_connection

    def import_data(self):
        self.database_connection.drop_databases()
        self.__insert_books_from_json()
        self.__create_users_from_json()
        self.__create_loans_from_json()

    def __insert_books_from_json(self):
        for book in self.data[self.books_entry_name]:
            cover_photo_path = self.data_json_folder + "/" + book[self.book_cover_photo]
            with open(cover_photo_path, 'rb') as f:
                cover_photo = f.read()
            book[self.book_cover_photo] = cover_photo
            self.database_connection.add_book_structure(book)

    def __create_users_from_json(self):
        for user in self.data[self.users_entry_name]:
            self.database_connection.add_user_structure(user)

    def __create_loans_from_json(self):
        for loan in self.data[self.loans_entry_name]:
            self.database_connection.add_loan_structure(loan)

