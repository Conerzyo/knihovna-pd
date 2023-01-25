from mongoDB.database_filler.DatabaseConnection import DatabaseConnection, Loan

from bson import ObjectId


class LoanAPI:
    def __init__(self, connection_string):
        self.db = DatabaseConnection(connection_string=connection_string)
        self.loans = []

    def getByUserId(self, userId):
        loan = self.db.get_all_loans_for_user(ObjectId(userId))

        if loan:
            self.loans.append(loan)
            return self.toJson()
        else:
            return {}

    def getActiveLoans(self, userId):
        loan = self.db.get_active_loans_for_user(ObjectId(userId))

        if loan:
            self.loans.append(loan)
            return self.toJson()
        else:
            return {}

    def getAllLoans(self):
        self.loans = self.db.get_all_loans()
        return self.toJson()

    def create(self, loan):
        return self.db.create_loan(loan=loan)

    def toJson(self):
        loans_list = []
        for loan in self.loans:
            loans_list.append({
                "id": str(loan.id),
                "bookId": str(loan.book_id),
                "userId": str(loan.user_id),
                "loanDate": loan.loan_date,
                "dueDate": loan.due_date,
                "endDate": loan.end_date})

        self.loans = []

        return {"loans": loans_list}
