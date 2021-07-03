from bs4 import BeautifulSoup

from scraper.locators.books_page_locators import BooksPageLocators
from scraper.parsers.books_parser import BookParser


class BooksPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        locator = BooksPageLocators.BOOK
        book_tags = self.soup.select(locator)
        return [BookParser(b) for b in book_tags]
