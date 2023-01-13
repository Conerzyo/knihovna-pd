import argparse
import traceback
import hashlib

from MongoFiller import MongoFiller
from DatabaseConnection import DatabaseConnection, User, Loan


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

        #database fill (reset)
        filler = MongoFiller(database_connection=databaseConnection, data_file=args.source_file)
        filler.import_data()

        #registration
        new_user = User()
        new_user.username = "some_random_username"
        new_user.hash = password_hash("1234")
        new_user.first_name = "Ladislav"
        new_user.last_name = "Vzpurný"
        new_user.social_number = "01234a8"
        new_user.address = "Jihlavská 69, Jihlava"
        registration_successful = databaseConnection.create_user(new_user)

        if registration_successful:
            print(f"Registration of {new_user.username} was successful.")
        else:
            print(f"Registration of {new_user.username} was not successful.")

        #get all books
        all_books = databaseConnection.get_all_books()

        for book in all_books:
            print(f"Found book {book.title}")

        #new loan
        main_guy = databaseConnection.get_user_by_username("main_guy")
        book = databaseConnection.get_book_by_title("Catch-22")

        loan = Loan()
        loan.user_id = main_guy.id
        loan.book_id = book.id

        creation_successful = databaseConnection.create_loan(loan)

        if creation_successful:
            print(f"Loan creation was successful.")
        else:
            print(f"Loan creation was not successful.")


        #get all loans
        all_loans = databaseConnection.get_all_loans()

        #end loan
        success = databaseConnection.end_loan(all_loans[0])

        if success:
            print(f"Loan return was successful.")
        else:
            print(f"Loan return was not successful.")

        #all loans for user
        all_loans_for_user = databaseConnection.get_all_loans_for_user(main_guy.id)
        print(f"Main guy has {len(all_loans)} loans")

        #active loans for user
        all_loans_active_for_user = databaseConnection.get_active_loans_for_user(main_guy.id)
        print(f"Main guy has {len(all_loans_active_for_user)} active loans")

        #get all users
        all_users = databaseConnection.get_all_users()
        print(f"Found {len(all_users)} users.")

        #activate user
        not_active_user = databaseConnection.get_user_by_username(new_user.username)
        success = databaseConnection.activate_user(not_active_user.id)

        if success:
            print(f"User {not_active_user.username} was activated.")
        else:
            print(f"User {not_active_user.username} was not activated")

        #edit user?
        to_edit_user = databaseConnection.get_user_by_username(new_user.username)
        to_edit_user.address = "This address have been modified"
        success = databaseConnection.edit_user(to_edit_user)

        if success:
            print(f"User {to_edit_user.username} was modified.")
        else:
            print(f"User {to_edit_user.username} was not modified")

        #data export !hash
        print("TODO")

        #data import !hash
        print("TODO")

        #book search
        books = databaseConnection.find_books(title="Catch-22")
        print(f"Found {len(books)} with title Catch-22")

        #user search
        users = databaseConnection.find_users(first_name="Ladislav")
        print(f"Found {len(users)} with name ladislav")

        #login
        logged_in_user_or_none = databaseConnection.login("main_guy", password_hash("1234"))
        if logged_in_user_or_none is not None:
            print(f"Login for {logged_in_user_or_none.username} was successful.")
        else:
            print(f"Login was not successful.")
    except Exception as e:
        print("Error occurred:\n")
        print(traceback.format_exc())

#todo reverzní index v mongoDB