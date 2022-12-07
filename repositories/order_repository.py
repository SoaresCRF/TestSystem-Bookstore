from entities.order import Order


class OrderRepository:
    def __init__(self):
        self.list_orders: list[Order] = []

    def append_order(self, order: Order) -> None:
        self.list_orders.append(order)

    def get_orders(self) -> list[Order]:
        return self.list_orders

    def __str__(self) -> str:
        formatText = "{0:<15} {1:<15} {2:<15} {3:<15} {4:<15}\n"
        str_orders = formatText.format("Id order", "Id cliente", "Nome", "Data", "Total preço")

        for order in self.list_orders:
            str_orders += formatText.format(order.id, order.customer.id, order.customer.name, order.date_order,
                                            order.total_price)
        return str_orders

    def verif_if_order_exists(self, order_id: int) -> bool:
        for order in self.list_orders:
            if order.id == order_id:
                return True
        return False

    def get_order(self, order_id: int):
        for order in self.list_orders:
            if order.id == order_id:
                return order
        return "Order not found!"
