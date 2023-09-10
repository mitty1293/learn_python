from iterator.iterator import Iterator
from iterator.bookshelf import BookShelf


class BookShelfIterator(Iterator):
    def __init__(self, bookshelf: BookShelf) -> None:
        self.bookshelf = bookshelf
        self.index = 0

    def has_next(self) -> bool:
        if self.index < self.bookshelf.number_of_books:
            return True
        return False

    def next(self):
        book = self.bookshelf.get_book(self.index)
        self.index += 1
        return book
