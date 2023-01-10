import argparse
import traceback
import hashlib

from MongoFiller import MongoFiller
from DatabaseConnection import DatabaseConnection


def password_hash( password):
    hasher = hashlib.md5()
    hasher.update(password.encode('utf-8'))
    return hasher.hexdigest()

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(
            prog='MongoDBFiller',
            description='Let\'s fill the DB!',
            epilog='or not.')
        parser.add_argument('--source_file', type=str)
        parser.add_argument("--connection_string", type=str)

        args = parser.parse_args()

        databaseConnection = DatabaseConnection(connection_string=args.connection_string)

        filler = MongoFiller(database_connection=databaseConnection, data_file=args.source_file)
        filler.import_data()

        #login example
        login = databaseConnection.login("mikew_the_jokester", password_hash("1234"))
    except Exception as e:
        print("Error occurred:\n")
        print(traceback.format_exc())

#todo reverzní index v mongoDB