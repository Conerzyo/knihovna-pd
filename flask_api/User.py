from DatabaseConnection import DatabaseConnection, UserSort

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

    def edit(self, userId, user):
        user_db = self.db.get_user_by_id(ObjectId(userId))
        if user.first_name is not None:
            user_db.first_name = user.first_name
        if user.last_name is not None:
            user_db.last_name = user.last_name
        if user.social_number is not None:
            user_db.social_number = user.social_number
        if user.address is not None:
            user_db.address = user.address
        if user.hash is not None:
            user_db.hash = user.hash

        return self.db.edit_user(user=user_db)

    def findUsers(self, first_name, last_name, address, social_number, sort_by):
        self.users = self.db.find_users(first_name=first_name,
                                        last_name=last_name,
                                        address=address,
                                        social_number=social_number,
                                        user_sort=UserSort.FIRST_NAME)

        return self.toJson()

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
