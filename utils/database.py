from utils.db_connection import DatabaseConnection


DATABASE_FILE = 'data.db'


def create_database_table():
    with DatabaseConnection(DATABASE_FILE) as connection:
        cursor = connection.cursor()

        cursor.execute(
            'CREATE TABLE IF NOT EXISTS books(title text primary key, author text, is_read integer)')


def add_book(title, author):
    """ Adds book to a collection.

    :param title: title of the book
    :param author: author of the book
    :return: True if succesfully added.
    """
    with DatabaseConnection(DATABASE_FILE) as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (title, author))


def remove_book(title, author):
    """ Removes book from collection.

    :return: True if succesfully removed.
    """
    with DatabaseConnection(DATABASE_FILE) as connection:
        cursor = connection.cursor()

        cursor.execute(
            'DELETE FROM books WHERE title=? AND author =?', (title, author))

        return cursor.rowcount == 1


def mark_book_as_read(title, author):
    """ Removes book from collection.

    :return: True if succesfully marked book as read.
    """
    with DatabaseConnection(DATABASE_FILE) as connection:
        cursor = connection.cursor()

        cursor.execute(
            'UPDATE books SET is_read=1 WHERE title=? AND author =?', (title, author))
            
        return cursor.rowcount == 1


def get_books():
    with DatabaseConnection(DATABASE_FILE) as connection:
        cursor = connection.cursor()

        books = [{'title': row[0], 'author': row[1], 'is_read': row[2]}
                for row in cursor.fetchall()]

        return books
