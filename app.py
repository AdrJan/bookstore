from utils import database


def print_instructions():
    print(""" Instructions: 
    Press (l) - listing all books
    Press (la) - listing books by author
    Press (a) - add book to collection
    Press (r) - remove book from collection
    Press (mr) - mark book as read
    Press (q) - quits """)


menu_options = {
    'a': database.add_book,
    'r': database.remove_book,
    'l': database.print_all_books,
    'la': database.print_books_by_author,
    'mr': database.mark_book_as_read
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
