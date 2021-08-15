# BOOKSTORE

_Application for keeping info about your books._

## User stories

* User can add new books to collections, so he can keep track what books he owns

* User can list all books in his collections, so he can see what books he already have.

* User can find a book using book title, or author.

## Technologies

* Python 3.9.1
* Flask, Jinja
* Html, CSS

## Setup

First of all make sure you have installed pipenv:

```
$ pip install pipenv
```

Then in project directory type in terminal:

```
$ pipenv shell
$ pipenv run python app.py
```

Application should be running in virtual env on your localhost: http://127.0.0.1:5000/

## Screenshots

![obraz](https://user-images.githubusercontent.com/23117274/129477695-5b40ffa9-d53f-4a07-916a-5d92c854a3a7.png)

_pic.1 Search book page_

![obraz](https://user-images.githubusercontent.com/23117274/129477733-dd70f90f-58b6-4c81-bda6-5eca1ebded65.png)

_pic.2 List books page_
## Configuration

Configuration file is placed in configuration folder:

```
[pages]
BOOKS_PER_PAGE = 2

[database]
DATABASE_FILE = data.db
```
_<p align="right">config.ini</p>_

where:

* BOOKS_PER_AGE -  Number of displayed books
* DATABASE_FILE -  Name of database file
