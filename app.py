# FUNCTIONS

def add_book(books, title, author):
    books.append({
        'title': title,
        'author': author
    })


def remove_book(books, title, author):
    return [
        book for book in books
        if not(book['title'] == title and book['author'] == author)
    ]


def print_all_books(books):
    for book in books:
        print(f'Title: {book["title"]}, author: {book["author"]}')
    else:
        print(f'Totally: {len(books)} books.')


def print_instructions():
    print('Instructions: ')
    print('Press (l) - listing your books')
    print('Press (a) - add book to collection')
    print('Press (r) - remove books from collection')
    print('Press (q) - quits')


def run_menu(books):
    print('================== BOOKSTORE ===================')
    print('This is your bookstore program.')
    print_instructions()
    input_op = input('Select option: ')
    while input_op != 'q':
        if input_op == 'a':
            new_book_title = input('Type title of the book: ')
            new_book_author = input('Type author of the book: ')
            add_book(books, new_book_title, new_book_author)
            print('*** You have added new book to the store. ***') 
            print(f'*** Title: "{new_book_title}", author: "{new_book_author}" ***')
        elif input_op == 'r':
            book_to_remove_title = input('Type title of the book to remove: ')
            book_to_remove_author = input('Type author of the book to remove: ')
            books_size = len(books)
            books = remove_book(books, book_to_remove_title, book_to_remove_author)
            if books_size == len(books):
                print('*** There is no such a book. Book has not been removed. ***')
            else:
                print('*** Book has been removed. ***')
        elif input_op == 'l':
            print_all_books()
        else:
            print('*** Unknown instruction. Select option from below. ***')
            print_instructions()
        input_op = input('\nSelect option: ')
    else:
        print('================================================')


# PROGRAM

run_menu([])
