from typing import Dict, List, Union
from utils.db_connection import DatabaseConnection


DATABASE_FILE = 'data.db'


def create_database_table() -> None:
    with DatabaseConnection(DATABASE_FILE) as connection:
        cursor = connection.cursor()

        cursor.execute(
            'CREATE TABLE IF NOT EXISTS books(title text primary key, author text, is_read integer)')


def add_book(title: str, author: str) -> bool:
    """ Adds book to a collection.

    :param title: title of the book
    :param author: author of the book
    :return: True if succesfully added.
    """
    with DatabaseConnection(DATABASE_FILE) as connection:
        cursor = connection.cursor()

        cursor.execute(
            'SELECT * FROM books WHERE title=? AND author=?', (title, author))
        if (cursor.rowcount > 0):
            return False
        else:
            cursor.execute('INSERT INTO books VALUES(?, ?, 0)',
                           (title, author))
            return True


def remove_book(title: str, author: str) -> bool:
    """ Removes book from collection.

    :return: True if succesfully removed.
    """
    with DatabaseConnection(DATABASE_FILE) as connection:
        cursor = connection.cursor()

        cursor.execute(
            'DELETE FROM books WHERE title=? AND author =?', (title, author))

        return cursor.rowcount == 1


def mark_book_as_read(title: str, author: str) -> bool:
    """ Removes book from collection.

    :return: True if succesfully marked book as read.
    """
    with DatabaseConnection(DATABASE_FILE) as connection:
        cursor = connection.cursor()

        cursor.execute(
            'UPDATE books SET is_read=1 WHERE title=? AND author =?', (title, author))

        return cursor.rowcount == 1


def get_books() -> List[Dict[str, Union[str, int]]]:
    with DatabaseConnection(DATABASE_FILE) as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')

        books = [{'title': row[0], 'author': row[1], 'is_read': row[2]}
                 for row in cursor.fetchall()]

        return books
