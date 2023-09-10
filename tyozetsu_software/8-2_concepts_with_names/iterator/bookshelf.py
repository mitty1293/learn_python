from iterator.aggregate import Aggregate
from iterator.bookshelf_iterator import BookShelfIterator


class Book:
    def __init__(self, name, pages) -> None:
        self.name = name
        self.pages = pages

    @property
    def name(self):
        return self.name

    @property
    def pages(self):
        return self.pages


class BookShelf(Aggregate):
    def __init__(self, max_size: int) -> None:
        self.books = [None] * max_size

    def iterator(self) -> BookShelfIterator:
        return BookShelfIterator(self)
    
    def add_book(self, book: Book):
        self.books.append(book)

    def get_book(self, index):
        return self.books[index]
    
    @property
    def number_of_books(self)
        return len(self.books)
    


