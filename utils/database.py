import sqlite3
from json.decoder import JSONDecodeError


FILE_NAME = 'books.json'
books = []


def create_database_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, is_read integer)')

    connection.commit()
    connection.close()

def save():
    with open(FILE_NAME, 'w') as f:
        # json.dump(books, f)
        pass

def _get_books_from_file():
    try:
        with open(FILE_NAME, 'r') as f:
            try:
                # return json.load(f)
                pass
            except JSONDecodeError:
                return []
    except FileNotFoundError:
        return []


def add_book(title, author):
    """ Adds book to a collection.

    :param title: title of the book
    :param author: author of the book
    """
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (title, author))

    connection.commit()
    connection.close()


def remove_book(title, author):
    """ Removes book from collection.

    :return: True if succesfully removed.
    """
    global books
    books_size = len(books)
    books = [
        book for book in books
        if not(book['title'] == title and book['author'] == author)
    ]

    return books_size != len(books)


def mark_book_as_read(title, author):
    """ Removes book from collection.

    :return: True if succesfully marked book as read.
    """
    is_marked = False
    for book in books:
        if (book['title'] == title and book['author'] == author):
            book['is_read'] = True
            is_marked = True

    return is_marked


def get_books():
    return books
