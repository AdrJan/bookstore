from utils import database
from scraper.pages.books_page import BooksPage
from flask import Flask, render_template, request, url_for, redirect
import requests


# FUNCTIONS
    
    
def get_books_from_pages() -> None:
    books = []
    urls = []
    for i in range(1, get_pages_num() + 1):
        urls.append(f'https://books.toscrape.com/catalogue/page-{i}.html')
    books = async_scraping.get_books(*urls)
    books = sorted(books, key=lambda x: x.rating * -1)
    for book in books:
        print(book)

    print('================================================')
    print('Summary:\n')
    print(f'Number of books: {len(books)}')
    print(f'Average rating: {(sum(book.rating for book in books) / len(books)):.2f}')


def get_pages_num() -> int:
    page_content = requests.get('https://books.toscrape.com').content
    page = BooksPage(page_content)
    return page.pages_num


app = Flask(__name__)


@app.route('/books', methods=['POST', 'GET'])
def books():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        if request.form['button_submit'] == 'delete':
            database.remove_book(title, author)
        elif request.form['button_submit'] == 'update':
            database.toggle_read(title, author)


        return redirect(url_for('books'))
        
    return render_template('books.jinja2', books = database.get_books())


@app.route('/add_book', methods=['POST', 'GET'])
def add_book():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        database.add_book(title, author)

        return redirect(url_for('books'))

    return render_template('add_book.jinja2')


if __name__ == '__main__':
    app.run(debug=True)
