books = []


def add_book(title, author):
    books.append({
        'title': title,
        'author': author
    })


def list_all_books():
    print('======== BOOKS =========')
    for book in books:
        print(f'Title: {book["title"]}, author: {book["author"]}')
    else:
        print(f'Totally: {len(books)} books.')
    print('=======================')


#TESTING
add_book('Lord of the rings', 'J.R.R Tolkien')
add_book('Hobbit', 'J.R.R. Tolkien')
add_book('Harry Potter and the hilosophers stone', 'J.K. Rowling')

list_all_books()
