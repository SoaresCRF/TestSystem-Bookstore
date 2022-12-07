import unittest
from entities.customer import Customer
from repositories.customer_repository import CustomerRepository


class MyTestCase(unittest.TestCase):
    def test_verif_if_customer_exists(self):
        customer_resp = CustomerRepository()

        customer_resp.add_customer(Customer(1, "Matheus"))

        self.assertTrue(customer_resp.verif_if_customer_exists(1))
        self.assertFalse(customer_resp.verif_if_customer_exists(2))

    def test_get_customer(self):
        customer_resp = CustomerRepository()

        customer_resp.add_customer(Customer(1, "Matheus"))

        self.assertTrue(customer_resp.get_customer(1).id == 1)
        self.assertTrue(customer_resp.get_customer(1).name == "Matheus")

        self.assertTrue(customer_resp.get_customer(-1).id == -1)
        self.assertTrue(customer_resp.get_customer(-1).name == "Client not found!")


if __name__ == '__main__':
    unittest.main()
