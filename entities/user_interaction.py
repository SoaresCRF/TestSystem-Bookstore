from datetime import date
from entities.fileCsv import FileCsv
from entities.book import Book
from entities.customer import Customer
from entities.order import Order
from repositories.customer_repository import CustomerRepository
from repositories.order_repository import OrderRepository
from repositories.book_repository import BookRepository


class UserInteraction:
    def __init__(self):
        self.customer_resp = CustomerRepository()
        self.order_resp = OrderRepository()
        self.book_resp = BookRepository()
        self.csv = FileCsv()

    def get_user_input(self) -> int:
        try:
            print("1 - Cadastrar cliente")
            print("2 - Fazer pedido")
            print("3 - Relatório de Pedidos")
            print("4 - Relatório de Clientes")
            print("5 - Relatório de Livros")
            print("0 - Sair")
            opcao = int(input("Informe a opção: "))
        except:
            opcao = -1
        return opcao

    def get_opcao_by_user(self) -> bool:
        result = self.get_user_input()

        if self.check_if_opcao_exists(result):
            if result == 0:
                print("Programa encerrado...")
                return False
            elif result == 1:
                return self.cadastrar_cliente()
            elif result == 2:
                return self.fazer_pedido()
            elif result == 3:
                return self.relatorio_pedidos()
            elif result == 4:
                return self.relatorio_clientes()
            else:
                return self.relatorio_livros()
        else:
            print("A opção informada é inválida, o programa vai ser encerrado...")
            return False

    def check_if_opcao_exists(self, result) -> bool:
        opcoes = [0, 1, 2, 3, 4, 5]
        for opcao in opcoes:
            if result == opcao:
                return True
        return False

    def cadastrar_cliente(self) -> bool:
        id_cliente = int(input("Informe o código do cliente: "))
        if self.customer_resp.verif_if_customer_exists(id_cliente):
            print("ID cliente já cadastrado!\n")
            return True

        nome = input("Informe o nome do cliente: ")

        self.customer_resp.list_customers.append(Customer(id_cliente, nome))

        print("Cliente cadastrado com sucesso!\n")
        return True

    def fazer_pedido(self) -> bool:
        id_pedido = int(input("Informe o código do pedido: "))
        if self.order_resp.verif_if_order_exists(id_pedido):
            print("ID pedido já cadastrado!\n")
            return True

        customer_id = int(input("Informe o código do cliente: "))
        if not self.customer_resp.verif_if_customer_exists(customer_id):
            print("Cliente não existe!\n")
            return True

        book_id = int(input("Informe o código do livro: "))
        if not self.book_resp.verif_if_book_exists(book_id, self.csv):
            print("Livro não existe!\n")
            return True

        if self.book_resp.verif_price(book_id, self.csv) == 0:
            print("Livro com preço indefinido!\n")
            return True

        book_qtd = int(input("Informe a quantidade a ser comprada: "))
        if not self.book_resp.verif_stock(book_id, book_qtd, self.csv):
            print("Estoque insuficiente!\n")
            return True

        book = self.book_resp.get_book(book_id, self.csv)
        order = Order(id_pedido, self.customer_resp.get_customer(customer_id), date.today())
        order.purchased_book = book
        self.book_resp.down_stock(book_qtd, book_id, self.csv)

        self.order_resp.list_orders.append(order)
        print("Pedido cadastrado com sucesso!\n")
        return True

    def relatorio_pedidos(self) -> bool:
        print("\n***** Relatório de pedidos *****\n")
        for order in self.order_resp.list_orders:
            print(f"Código do Pedido: {order.id}")
            print(f"Cliente: {order.customer.name}")
            print(f"Data do pedido: {order.date_order}")
            print(f"Livro escolhido: {order.purchased_book.name} \n")
        return True

    def relatorio_clientes(self) -> bool:
        print(f"\n***** Relatório de clientes *****\n"
              f"{self.customer_resp.__str__()}")
        return True

    def relatorio_livros(self) -> bool:
        print(f"\n***** Relatório de livros cadastrados *****\n"
              f"{self.csv.__str__()}")
        return True
