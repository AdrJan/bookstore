from utils import database
from flask import Flask, render_template, request, url_for, redirect
from configparser import ConfigParser


config = ConfigParser()
config.read('configuration/config.ini')

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


cached_title = ''
cached_author = ''


@app.route('/search_book', methods=['POST', 'GET'])
def search_book():
    books = []
    global cached_title
    global cached_author
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')

        if request.form['button_submit'] == 'delete':
            database.remove_book(title, author)
        elif request.form['button_submit'] == 'update':
            database.toggle_read(title, author)
        else:
            cached_title = title
            cached_author = author
        books = database.get_filtered_books(cached_title, cached_author)

    return render_template('search_book.jinja2', books=books)


if __name__ == '__main__':
    app.run(debug=True)
