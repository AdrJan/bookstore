from utils import database
from scraper.pages.books_page import BooksPage
import requests

# FUNCTIONS


def add_book():
    title = input('Type title of the book: ')
    author = input('Type author of the book: ')

    if database.add_book(title, author):
        print('*** You have added new book to the store. ***')
        print(f'*** Title: "{title}", author: "{author}" ***')
    else:
        print('*** You cant add another book with same title ***')


def remove_book():
    title = input('Type title of the book to remove: ')
    author = input('Type author of the book to remove: ')

    if database.remove_book(title, author):
        print('*** You have removed book from store. ***')
        print(f'*** Title: "{title}", author: "{author}" ***')
    else:
        print("*** There is no such book to remove! ***")


def mark_book_as_read():
    title = input('Type title of the book to mark as read: ')
    author = input('Type author of the book to mark as read: ')

    if database.mark_book_as_read(title, author):
        print('*** You have succesfully marked book as read. ***')
        print(f'*** Title: {title}, author: {author} ***')
    else:
        print("*** There is no such book to mark! ***")


def print_books(books):
    for book in books:
        is_read = 'YES' if book['is_read'] else 'NO'
        print(
            f'Title: {book["title"]}, author: {book["author"]}, marked as read: {is_read}')
    else:
        print(f'Totally: {len(books)} books.')


def print_all_books():
    print_books(database.get_books())


def print_books_by_author():
    author = input('Type author of the book: ')

    books = database.get_books()

    filtered_books = [
        book for book in books
        if book['author'] == author
    ]

    print_books(filtered_books)
    
# TODO: Add usage of get_pages_num
# now regex is not working
# value 51 (number of pages) is hardcoded
def get_books_from_pages() -> None:
    books = []
    for i in range(1, 51):
        books.extend(get_books_from_page(f'https://books.toscrape.com/catalogue/page-{i}.html'))
    books = sorted(books, key=lambda x: x.rating * -1)
    for book in books:
        print(book)

    print('================================================')
    print('Summary:\n')
    print(f'Number of books: {len(books)}')
    print(f'Average rating: {(sum(book.rating for book in books) / len(books)):.2f}')


def get_books_from_page(url) -> list:
    page_content = requests.get(url).content
    page = BooksPage(page_content)
    return page.books


def get_pages_num() -> int:
    page_content = requests.get('https://books.toscrape.com').content
    page = BooksPage(page_content)
    return page.pages_num


def print_instructions():
    print(""" Instructions: 
    Press (l) - listing all books
    Press (la) - listing books by author
    Press (a) - add book to collection
    Press (r) - remove book from collection
    Press (mr) - mark book as read
    Press (d) - show books from web (https://books.toscrape.com/)
    Press (q) - quits """)


menu_options = {
    'a': add_book,
    'r': remove_book,
    'mr': mark_book_as_read,
    'l': print_all_books,
    'la': print_books_by_author,
    'd': get_books_from_pages
}


def run():
    database.create_database_table()

    print('================== BOOKSTORE ===================')
    print('This is your bookstore program.')
    print_instructions()

    input_op = input('\nSelect option: ')
    while input_op != 'q':
        if input_op in menu_options:
            selected_operation = menu_options[input_op]
            selected_operation()
        else:
            print('*** Unknown instruction. Select option from below. ***')
            print_instructions()
        input_op = input('\nSelect option: ')
    else:
        print('================================================')


# PROGRAM

run()
