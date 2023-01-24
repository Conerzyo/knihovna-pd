from mongoDB.database_filler.DatabaseConnection import DatabaseConnection, Loan

from flask import Flask
from flask_restful import Api, Resource


class LoanAPI(Resource):
    def __init__(self, connection_string):
        self.db = DatabaseConnection(connection_string=connection_string)
        self.loans = []

    def toJson(self):
        loans_list = []
        for loan in self.loans:
            loans_list.append({
                "id": str(loan.id),
                "firstName": loan.first_name,
                "lastName": loan.last_name,
                "socialNumber": loan.social_number,
                "address": loan.address,
                "username": loan.username,
                "hash": loan.hash,
                "loanCount": loan.loan_count,
                "active": loan.active,
                "admin": loan.admin})
        return {"users": loans_list}
