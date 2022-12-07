from entities.book import Book


class FileCsv:
    def __init__(self):
        file_book = list(open("books.csv", "r", encoding="utf-8"))

        self.list_books: list[Book] = []

        def format_str_price_to_float(price: str) -> float:
            try:
                return float(price.replace("R$ ", "").replace(",", "."))
            except:
                return 0

        for book in file_book[1:]:
            list_book = book.split(";")
            book = Book(int(list_book[0]), list_book[1], list_book[2], list_book[3],
                        list_book[4], format_str_price_to_float(list_book[5]))
            self.list_books.append(book)

    def get_list_books(self):
        return self.list_books

    def __str__(self) -> str:
        formatText = "{0:<10} {1:<115} {2:<20} {3:<100} {4:<115} {5:<10} {6:<10}\n"
        str_books = formatText.format("Id livro", "Titulo", "Isbn", "Autor", "Categoria", "Valor", "Estoque")

        for book in self.list_books:
            str_books += formatText.format(book.id, book.name, book.isbn, book.author, book.category, book.price,
                                           book.stock)

        return str_books
