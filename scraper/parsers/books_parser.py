from scraper import locators
from scraper.locators.book_locators import BookLocators


class BookParser:
    rating_mapper = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self,  parent) -> None:
        self.parent = parent

    def __repr__(self) -> str:
        return f'<Book "{self.title}", price "{self.price}", rating {self.rating} stars. >'

    @property
    def title(self) -> str:
        locator = BookLocators.TITLE
        return self.parent.select_one(locator).string

    @property
    def price(self) -> str:
        locator = BookLocators.PRICE
        return self.parent.select_one(locator).string

    @property
    def rating(self) -> str:
        locator = BookLocators.RATING
        return self.rating_mapper[[
            r for r
            in self.parent.select_one(locator).attrs['class']
        ][1]]
