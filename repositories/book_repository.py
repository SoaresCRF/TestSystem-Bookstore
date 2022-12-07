from entities.book import Book
from entities.fileCsv import FileCsv


class BookRepository:
    def __init__(self):
        pass

    def verif_if_book_exists(self, book_id: int, file_csv: FileCsv) -> bool:
        for book in file_csv.get_list_books():
            if book.id == book_id:
                return True
        return False

    def verif_stock(self, book_id: int, qtd: int, file_csv: FileCsv) -> bool:
        for book in file_csv.get_list_books():
            if book.id == book_id:
                return book.stock >= qtd
        return False

    def verif_price(self, book_id: int, file_csv) -> float:
        for book in file_csv.get_list_books():
            if book.id == book_id:
                return book.price

    def down_stock(self, qtd: int, book_id: int, file_csv: FileCsv) -> None:
        for book in file_csv.get_list_books():
            if book.id == book_id:
                book.stock -= qtd

    def get_book(self, book_id: int, file_csv: FileCsv) -> Book:
        for book in file_csv.get_list_books():
            if book.id == book_id:
                return book
        return Book(-1, "Book not found!", "", "", "", 0)
