import unittest

from entities.customer import Customer
from repositories.customer_repository import CustomerRepository


class MyTestCase(unittest.TestCase):
    def test_cadastrar_cliente(self):
        customer_resp = CustomerRepository()
        id = 1
        if not customer_resp.verif_if_customer_exists(id):
            nome = "Matheus"
            customer_resp.list_customers.append(Customer(id, nome))

        if not customer_resp.verif_if_customer_exists(id):
            nome = "João"
            customer_resp.list_customers.append(Customer(id, nome))

        self.assertTrue(customer_resp.list_customers.__len__() == 1)


if __name__ == '__main__':
    unittest.main()
