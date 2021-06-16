books = []

def print_books(books):
    for book in books:
        print(f'Title: {book["title"]}, author: {book["author"]}')
    else:
        print(f'Totally: {len(books)} books.')


def add_book():
    title = input('Type title of the book: ')
    author = input('Type author of the book: ')

    books.append({
        'title': title,
        'author': author
    })

    print('*** You have added new book to the store. ***') 
    print(f'*** Title: "{title}", author: "{author}" ***')


def remove_book():
    title = input('Type title of the book to remove: ')
    author = input('Type author of the book to remove: ')

    global books
    books_size = len(books)
    books = [
        book for book in books
        if not(book['title'] == title and book['author'] == author)
    ]

    if books_size == len(books):
        print('*** There is no such a book. Book has not been removed. ***')
    else:
        print('*** Book has been removed. ***')


def print_all_books():
    print_books(books)


def print_books_by_author():
    author = input('Type author of the book: ')

    filtered_books = [
        book for book in books
        if book['author'] == author
    ]

    print_books(filtered_books)
