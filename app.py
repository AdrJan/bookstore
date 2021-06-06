books = []


def add_book(title, author):
    books.append({
        'title': title,
        'author': author
    })

#TESTING
add_book('Lord of the rings', 'J.R.R Tolkien')
add_book('Hobbit', 'J.R.R. Tolkien')
add_book('Harry Potter and the hilosophers stone', 'J.K. Rowling')

print(books)
