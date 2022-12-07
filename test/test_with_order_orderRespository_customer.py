import unittest
from datetime import date
from repositories.customer_repository import CustomerRepository
from entities.customer import Customer
from entities.order import Order
from repositories.order_repository import OrderRepository


class MyTestCase(unittest.TestCase):
    def test_fazer_pedido(self):
        cliente = Customer(1, "Matheus")
        customer_resp = CustomerRepository()
        order_resp = OrderRepository()

        self.assertTrue(order_resp.list_orders.__len__() == 0)
        self.assertFalse(order_resp.list_orders.__len__() == 1)

        order = Order(1, customer_resp.get_customer(cliente.id), date.today())
        order_resp.append_order(order)

        self.assertTrue(order_resp.verif_if_order_exists(1))
        self.assertFalse(order_resp.verif_if_order_exists(0))
        self.assertFalse(order_resp.list_orders.__len__() == 0)
        self.assertTrue(order_resp.list_orders.__len__() == 1)


if __name__ == '__main__':
    unittest.main()
