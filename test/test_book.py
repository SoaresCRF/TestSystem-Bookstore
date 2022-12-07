import unittest
from entities.fileCsv import FileCsv
from repositories.book_repository import BookRepository


class MyTestCase(unittest.TestCase):

    def test_verif_if_book_exists(self):
        file_csv = FileCsv()
        book_resp = BookRepository()

        self.assertTrue(book_resp.verif_if_book_exists(1, file_csv))
        self.assertFalse(book_resp.verif_if_book_exists(0, file_csv))

    def test_verif_stock(self):
        file_csv = FileCsv()
        book_resp = BookRepository()

        self.assertTrue(book_resp.verif_stock(1, 1, file_csv))
        self.assertFalse(book_resp.verif_stock(1, 2, file_csv))

    def test_down_stock(self):
        file_csv = FileCsv()
        book_resp = BookRepository()

        book = file_csv.list_books[0]
        book_resp.down_stock(1, book.id, file_csv)


        self.assertTrue(book.stock == 0)
        self.assertFalse(book.stock != 0)

    def test_get_book(self):
        file_csv = FileCsv()
        book_resp = BookRepository()

        self.assertTrue(book_resp.get_book(1, file_csv).id == 1)
        self.assertEquals(book_resp.get_book(1, file_csv).name, "50 Tons da Vida")
        self.assertEquals(book_resp.get_book(1, file_csv).isbn, "97-885-7480-817-8")
        self.assertEquals(book_resp.get_book(1, file_csv).author, "Roberto Livianu")
        self.assertEquals(book_resp.get_book(1, file_csv).category, "Literatura brasileira, Crônicas")
        self.assertTrue(book_resp.get_book(1, file_csv).price == 39.9)

        self.assertTrue(book_resp.get_book(-1, file_csv).id == -1)
        self.assertEquals(book_resp.get_book(-1, file_csv).name, "Book not found!")
        self.assertEquals(book_resp.get_book(-1, file_csv).isbn, "")
        self.assertEquals(book_resp.get_book(-1, file_csv).author, "")
        self.assertEquals(book_resp.get_book(-1, file_csv).category, "")
        self.assertTrue(book_resp.get_book(-1, file_csv).price == 0)


if __name__ == '__main__':
    unittest.main()
