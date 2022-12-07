import unittest
from datetime import date

from entities.customer import Customer
from entities.fileCsv import FileCsv
from entities.order import Order
from repositories.customer_repository import CustomerRepository
from repositories.order_repository import OrderRepository
from repositories.book_repository import BookRepository


class MyTestCase(unittest.TestCase):
    def test_fazer_pedido(self):
        order_resp = OrderRepository()
        cusomer_resp = CustomerRepository()
        book_resp = BookRepository()
        csv = FileCsv()

        cusomer_resp.list_customers.append(Customer(1, "Matheus"))
        id_pedido = 1
        if not order_resp.verif_if_order_exists(id_pedido):
            customer_id = 1
            if cusomer_resp.verif_if_customer_exists(customer_id):
                book_id = 1
                if book_resp.verif_if_book_exists(book_id, csv):
                    if book_resp.verif_price(book_id, csv) != 0:
                        book_qtd = 1
                        if book_resp.verif_stock(book_id, book_qtd, csv):
                            book = book_resp.get_book(book_id, csv)
                            order = Order(id_pedido, cusomer_resp.get_customer(customer_id),
                                          date.today())
                            order.purchased_book = book
                            book_resp.down_stock(book_qtd, book_id, csv)

                            order_resp.list_orders.append(order)
                            self.assertTrue(order_resp.list_orders.__len__() == 1)


if __name__ == '__main__':
    unittest.main()
