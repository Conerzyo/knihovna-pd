from mongoDB.database_filler.DatabaseConnection import DatabaseConnection

from bson import ObjectId

class UserAPI:

    def __init__(self, connection_string):
        self.db = DatabaseConnection(connection_string=connection_string)
        self.users = []

    def getByName(self, name):
        usr = self.db.get_user_by_username(name)

        if usr:
            self.users.append(usr)
            return self.toJson()
        else:
            return {}

    def getById(self, userId):
        usr = self.db.get_user_by_id(ObjectId(userId))

        if usr:
            self.users.append(usr)
            return self.toJson()
        else:
            return {}

    def getAllUsers(self):
        self.users = self.db.get_all_users()
        return self.toJson()

    def create(self, user):
        return self.db.create_user(user=user)

    def findUser(self, first_name, last_name, address, social_number):
        return {}

    def toJson(self):
        user_list = []
        for user in self.users:
            user_list.append({
                "id": str(user.id),
                "firstName": user.first_name,
                "lastName": user.last_name,
                "socialNumber": user.social_number,
                "address": user.address,
                "username": user.username,
                "loanCount": user.loan_count,
                "active": user.active,
                "admin": user.admin})

        self.users = []

        return {"users": user_list}
