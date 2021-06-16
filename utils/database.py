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


def print_books(books):
    for book in books:
        print(f'Title: {book["title"]}, author: {book["author"]}')
    else:
        print(f'Totally: {len(books)} books.')


def add_book():
    title = input('Type title of the book: ')
    author = input('Type author of the book: ')

    books = get_books_from_file()

    books.append({
        'title': title,
        'author': author
    })

    save_books_to_file(books)

    print('*** You have added new book to the store. ***')
    print(f'*** Title: "{title}", author: "{author}" ***')


def remove_book():
    title = input('Type title of the book to remove: ')
    author = input('Type author of the book to remove: ')

    books = get_books_from_file()

    books_size = len(books)
    books = [
        book for book in books
        if not(book['title'] == title and book['author'] == author)
    ]

    save_books_to_file(books)

    if books_size == len(books):
        print('*** There is no such a book. Book has not been removed. ***')
    else:
        print('*** Book has been removed. ***')


def print_all_books():
    print_books(get_books_from_file())


def print_books_by_author():
    author = input('Type author of the book: ')

    books = get_books_from_file()

    filtered_books = [
        book for book in books
        if book['author'] == author
    ]

    print_books(filtered_books)
