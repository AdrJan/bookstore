books = []

# FUNCTIONS

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
    for book in books:
        print(f'Title: {book["title"]}, author: {book["author"]}')
    else:
        print(f'Totally: {len(books)} books.')


def print_instructions():
    print('Instructions: ')
    print('Press (l) - listing your books')
    print('Press (a) - add book to collection')
    print('Press (r) - remove book from collection')
    print('Press (q) - quits')


menu_options = {
    'a': add_book,
    'r': remove_book,
    'l': print_all_books
}


def run_menu():
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

run_menu()
