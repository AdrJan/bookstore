from utils import database
from scraper.pages.books_page import BooksPage
from flask import Flask, render_template, request, url_for, redirect
from configparser import ConfigParser
import requests


config = ConfigParser()
config.read('configuration/config.ini')


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
    print(
        f'Average rating: {(sum(book.rating for book in books) / len(books)):.2f}')


def get_pages_num() -> int:
    page_content = requests.get('https://books.toscrape.com').content
    page = BooksPage(page_content)
    return page.pages_num


app = Flask(__name__)


@app.route('/books/<page_num>', methods=['POST', 'GET'])
def books(page_num):
    BOOKS_PER_PAGE = int(config.get('pages', 'BOOKS_PER_PAGE'))
    page_num = int(page_num)
    offset = page_num * BOOKS_PER_PAGE

    last_page = len(database.get_books()) / BOOKS_PER_PAGE - 1
    books = database.get_sliced_books(offset, BOOKS_PER_PAGE)

    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        if request.form['button_submit'] == 'delete':
            page_num = page_num if len(books) != 1 else page_num - 1
            page_num = 0 if page_num < 0 else page_num
            database.remove_book(title, author)
        elif request.form['button_submit'] == 'update':
            database.toggle_read(title, author)

        return redirect(url_for('books', page_num=page_num))

    return render_template('books.jinja2', books=books, page_num=page_num, last_page=last_page)


@app.route('/add_book', methods=['POST', 'GET'])
def add_book():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        database.add_book(title, author)

        return redirect(url_for('books', page_num=0))

    return render_template('add_book.jinja2')


@app.route('/search_book', methods=['POST', 'GET'])
def search_book():
    books = []
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        
        # TODO fix, search is blank after mark/delete
        if request.form['button_submit'] == 'delete':
            database.remove_book(title, author)
        elif request.form['button_submit'] == 'update':
            database.toggle_read(title, author)
        else:
            books = database.get_filtered_books(title, author)

    return render_template('search_book.jinja2', books=books)


if __name__ == '__main__':
    app.run(debug=True)
