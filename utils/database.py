import sqlite3


DATABASE_FILE = 'data.db'


def create_database_table():
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute(
        'CREATE TABLE IF NOT EXISTS books(title text primary key, author text, is_read integer)')

    connection.commit()
    connection.close()


def add_book(title, author):
    """ Adds book to a collection.

    :param title: title of the book
    :param author: author of the book
    :return: True if succesfully added.
    """
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    try:
        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (title, author))
        connection.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        connection.close()


def remove_book(title, author):
    """ Removes book from collection.

    :return: True if succesfully removed.
    """
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute(
        'DELETE FROM books WHERE title=? AND author =?', (title, author))

    connection.commit()
    connection.close()
    return cursor.rowcount == 1


def mark_book_as_read(title, author):
    """ Removes book from collection.

    :return: True if succesfully marked book as read.
    """
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute(
        'UPDATE books SET is_read=1 WHERE title=? AND author =?', (title, author))

    connection.commit()
    connection.close()
    return cursor.rowcount == 1


def get_books():
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    books = [{'title': row[0], 'author': row[1], 'is_read': row[2]}
             for row in cursor.fetchall()]

    return books
