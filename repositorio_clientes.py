from Cliente.cliente import Cliente


class Repositorio_Cliente(Cliente):

    def __init__(self):
        self.clientes = []


    def cadastrar(self, cliente: Cliente):
        self.clientes.append(cliente)

    def buscar(self, cpf):
        for cliente in self.clientes:
            if cliente.get_nomecliente() == cliente:
                return cliente
            else:
                return None

    def atualizar(self, cliente: Cliente):
        pass

    def listar(self):
        pass