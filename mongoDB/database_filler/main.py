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
        parser.add_argument('--source_file', type=str)
        parser.add_argument("--connection_string", type=str)

        args = parser.parse_args()

        databaseConnection = DatabaseConnection(connection_string=args.connection_string)

        filler = MongoFiller(database_connection=databaseConnection, data_file=args.source_file)
        filler.import_data()
    except Exception as e:
        print("Error occurred:\n")
        print(traceback.format_exc())

#todo reverzní index v mongoDB