from clientej import Cliente


class RepositorioCliente:

    def __init__(self):
        self.clientes = []

    def cadastrar(self, cliente: Cliente):
        self.clientes.append(cliente)

    def buscar(self, cpf):
        for cliente in self.clientes:
            if cliente.get_cpf() == cpf:
                return cliente
            else:
                return None

    def atualizar(self, cliente: Cliente):
        cliente = self.buscar(cliente.get_cpf())
        if cliente is not None:
            cliente.set_nome(cliente.get_name())
            cliente.set_endereco(cliente.get_endereco())
        else:
            print("Cliente inexistente!")


    def listar(self):
        pass

