import re
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

    @property
    def pages_num(self) -> int:
        locator = BooksPageLocators.PAGES_NUM
        pages_num_str = self.soup.select_one(locator).string
        return int(re.findall('([0-9]+)', pages_num_str)[-1])
