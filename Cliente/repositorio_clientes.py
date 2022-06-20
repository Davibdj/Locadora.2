from Cliente.cliente import Cliente


class RepositorioCliente:

    def __init__(self):
        self.clientes = []

    def cadastrar(self, cliente: Cliente):
        if self.buscar(cliente.get_cpf()) is None:
            self.clientes.append(cliente)
            print("Cadastro Realizado com sucesso!")
        else:
            print("Cliente já cadastrado.")

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
        return print(' '. join(self.clientes))