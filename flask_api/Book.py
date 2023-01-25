from mongoDB.database_filler.DatabaseConnection import DatabaseConnection, Book

from bson import ObjectId


class BookAPI:
    def __init__(self, connection_string):
        self.db = DatabaseConnection(connection_string=connection_string)
        self.books = []

    def getByTitle(self, title):
        usr = self.db.get_book_by_title(title)

        if usr:
            self.books.append(usr)
            return self.toJson()
        else:
            return {}

    def getById(self, bookId):
        book = self.db.get_book_by_id(ObjectId(bookId))

        if book:
            self.books.append(book)
            return self.toJson()
        else:
            return {}

    def getAllBooks(self):
        self.books = self.db.get_all_books()
        return self.toJson()

    def create(self, book):
        return self.db.create_book(book=book)

    def findBook(self, title, year, author):
        return {}

    def toJson(self):
        book_list = []
        for book in self.books:
            book_list.append({
                "id": str(book.id),
                "title": book.title,
                "author": book.author,
                "year": book.year,
                "pages": book.pages,
                "countOverall": book.count_overall,
                "countAvailable": book.count_available})

        self.books = []

        return {"books": book_list}
