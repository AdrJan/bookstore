from typing import Dict, List, Union
from utils.db_connection import DatabaseConnection
from configparser import ConfigParser


config = ConfigParser()
config.read('configuration/config.ini')

DATABASE_FILE = config.get('database', 'DATABASE_FILE')


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


def get_filtered_books(title: str, author: str) -> List[Dict[str, Union[str, int]]]:
    with DatabaseConnection(DATABASE_FILE) as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM books WHERE title LIKE ? AND author LIKE ?",
                       ('%'+title+'%', '%'+author+'%'))
        books = [{'title': row[0], 'author': row[1], 'is_read': row[2]}
                 for row in cursor.fetchall()]

        return books


def toggle_read(title: str, author: str) -> bool:
    """ Removes book from collection.

    :return: True if succesfully marked book as read.
    """
    with DatabaseConnection(DATABASE_FILE) as connection:
        cursor = connection.cursor()

        cursor.execute(
            'SELECT is_read FROM books WHERE title=? AND author=?', (title, author))
        is_read = 0 if cursor.fetchone()[0] else 1
        cursor.execute(
            'UPDATE books SET is_read=? WHERE title=? AND author=?', (is_read, title, author))

        return cursor.rowcount == 1


def get_books() -> List[Dict[str, Union[str, int]]]:
    with DatabaseConnection(DATABASE_FILE) as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        books = [{'title': row[0], 'author': row[1], 'is_read': row[2]}
                 for row in cursor.fetchall()]

        return books


def get_sliced_books(offset, limit) -> List[Dict[str, Union[str, int]]]:
    with DatabaseConnection(DATABASE_FILE) as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books LIMIT ? OFFSET ?', (limit, offset))
        books = [{'title': row[0], 'author': row[1], 'is_read': row[2]}
                 for row in cursor.fetchall()]

        return books
