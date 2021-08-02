import asyncio

import aiohttp

from scraper.pages.books_page import BooksPage


async def fetch_page(session, url):
    async with session.get(url) as response:
        return await response.text()


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        return await asyncio.gather(*tasks)
        

def get_books(*urls):
    books = []
    loop = asyncio.get_event_loop()
    pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
    for page in pages:
        books.extend(BooksPage(page).books)
    return books
