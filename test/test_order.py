import unittest
from repositories.order_repository import OrderRepository


class MyTestCase(unittest.TestCase):
    def test_verif_if_order_exists(self):
        order_resp = OrderRepository()
        self.assertFalse(order_resp.verif_if_order_exists(1))  # add assertion here


if __name__ == '__main__':
    unittest.main()
