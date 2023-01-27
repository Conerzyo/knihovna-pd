from DatabaseConnection import DatabaseConnection, Loan

from bson import ObjectId

from User import UserAPI
from Book import BookAPI


class LoanAPI:
    def __init__(self, connection_string):
        self.db = DatabaseConnection(connection_string=connection_string)
        self.loans = []
        self.conStr = connection_string

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

    def getById(self, loanId):
        loan = self.db.get_loan_by_id(ObjectId(loanId))
        return loan

    def create(self, loan):
        return self.db.create_loan(loan=loan)

    def endLoan(self, loan):
        return self.db.end_loan(loan=loan)

    def toJson(self):
        loans_list = []
        userApi = UserAPI(connection_string=self.conStr)
        bookApi = BookAPI(connection_string=self.conStr)


        for loan in self.loans:
            user = userApi.getById_loan(str(loan.user_id))
            book = bookApi.getById_loan(str(loan.book_id))

            loans_list.append({
                "id": str(loan.id),
                "book": book,
                "user": user,
                "loanDate": loan.loan_date,
                "dueDate": loan.due_date,
                "endDate": loan.end_date})

        self.loans = []

        return {"loans": loans_list}
