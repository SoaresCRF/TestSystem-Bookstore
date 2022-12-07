from entities.customer import Customer


class CustomerRepository:

    def __init__(self):
        self.list_customers: list[Customer] = []

    def add_customer(self, customer: Customer) -> None:
        self.list_customers.append(customer)

    def get_list_customers(self) -> list:
        return self.list_customers

    def verif_if_customer_exists(self, customer_id: int) -> bool:
        for customer in self.list_customers:
            if customer.id == customer_id:
                return True
        return False

    def get_customer(self, customer_id: int):
        for customer in self.list_customers:
            if customer.id == customer_id:
                return customer
        return Customer(-1, "Client not found!")

    def __str__(self) -> str:
        formatText = "{0:<15} {1:<15}\n"
        str_customers = formatText.format("Id cliente", "Nome")

        for customer in self.list_customers:
            str_customers += formatText.format(customer.id, customer.name)

        return str_customers
