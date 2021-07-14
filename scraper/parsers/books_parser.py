import re
from scraper.locators.book_locators import BookLocators


class BookParser:

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self,  parent) -> None:
        self.parent = parent

    def __repr__(self) -> str:
        return f'<Book "{self.title}", price "£{self.price} ", rating {self.rating} stars. >'

    @property
    def title(self) -> str:
        locator = BookLocators.TITLE
        return self.parent.select_one(locator).attrs['title']

    @property
    def price(self) -> float:
        locator = BookLocators.PRICE
        priceStr = self.parent.select_one(locator).string
        return float(re.search('[0-9]*\.[0-9]*', priceStr).group())

    @property
    def rating(self) -> str:
        locator = BookLocators.RATING
        return BookParser.RATINGS[[
            r for r
            in self.parent.select_one(locator).attrs['class']
        ][1]]
    