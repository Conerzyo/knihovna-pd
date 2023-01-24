from mongoDB.database_filler.DatabaseConnection import DatabaseConnection

from flask import Flask
from flask_restful import Api, Resource


class AdminAPI(Resource):

    def __init__(self, connection_string):
        self.db = DatabaseConnection(connection_string=connection_string)


