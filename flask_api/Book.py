from mongoDB.database_filler.DatabaseConnection import DatabaseConnection, Book

from flask import Flask
from flask_restful import Api, Resource


class BookAPI(Resource):

    def __init__(self, connection_string):
        self.db = DatabaseConnection(connection_string=connection_string)
        self.books = []

    def toJson(self):
        user_list = []
        for book in self.books:
            user_list.append({
                "id": str(book.id),
                "firstName": book.first_name,
                "lastName": book.last_name,
                "socialNumber": book.social_number,
                "address": book.address,
                "username": book.username,
                "hash": book.hash,
                "loanCount": book.loan_count,
                "active": book.active,
                "admin": book.admin})
        return {"users": user_list}
