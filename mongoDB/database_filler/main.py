import argparse
import traceback

from MongoFiller import MongoFiller
from DatabaseConnection import DatabaseConnection


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(
            prog='MongoDBFiller',
            description='Let\'s fill the DB!',
            epilog='or not.')
        parser.add_argument('--host', type=str)
        parser.add_argument('--port', type=int)
        parser.add_argument('--username', type=str)
        parser.add_argument('--password', type=str)
        parser.add_argument('--source_file', type=str)

        args = parser.parse_args()

        databaseConnection = DatabaseConnection(host=args.host, port=args.port, username=args.username, password=args.password)

        filler = MongoFiller(database_connection=databaseConnection, data_file=args.source_file)
        filler.import_data()
    except Exception as e:
        print("Error occurred:\n")
        print(traceback.format_exc())

#todo reverzní index v mongoDB