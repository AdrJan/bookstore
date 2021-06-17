import json
from json.decoder import JSONDecodeError


def save_books_to_file(books):
    with open('books.txt', 'w') as f:
        json.dump(books, f)


def get_books_from_file():
    with open('books.txt', 'r') as f:
        try:
            return json.load(f)
        except JSONDecodeError:
            return []


def add_book(title, author):
    """ Adds book to a collection.

    :param title: title of the book
    :param author: author of the book
    """
    books = get_books_from_file()

    books.append({
        'title': title,
        'author': author,
        'is_read': False
    })

    save_books_to_file(books)


def remove_book(title, author):
    """ Removes book from collection.

    :return: True if succesfully removed.
    """
    books = get_books_from_file()

    books_size = len(books)
    books = [
        book for book in books
        if not(book['title'] == title and book['author'] == author)
    ]

    save_books_to_file(books)

    return books_size != len(books)


def mark_book_as_read(title, author):
    """ Removes book from collection.

    :return: True if succesfully marked book as read.
    """
    books = get_books_from_file()

    is_marked = False
    for book in books:
        if (book['title'] == title and book['author'] == author):
            book['is_read'] = True
            is_marked = True

    save_books_to_file(books)

    return is_marked
