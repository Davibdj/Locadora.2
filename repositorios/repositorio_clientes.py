from Cliente.cliente import Cliente


class RepositorioCliente:

    def __init__(self):
        self.clientes = []  # Inicializando uma lista

    def cadastrar(self, cliente: Cliente):
        if self.buscar(cliente.get_cpf()) is None:  # Buscando o cliente pelo número do cpf, e se não for nada:
            self.clientes.append(cliente)  # Adiciona o cliente a lista cliente
            print("Cadastro Realizado com sucesso!")
        else:
            print("Cliente já cadastrado.")

    def buscar(self, cpf):
        for cliente in self.clientes:  # Percorre os elementos da lista Clientes
            if cliente.get_cpf() == cpf:  # Verifica se o cpf passado é igual a algum da lista clientes
                return cliente  # Retorna o cliente
            else:
                return None

    def atualizar(self, cliente: Cliente):
        cliente = self.buscar(
            cliente.get_cpf())  # Procurando um cliente pelo metodo buscar(verifica o numero do cpf na lista cliente), pelo cpf e atribui a cliente
        if cliente is not None:  # Se o cliente não for nulo então:
            cliente.set_nome(cliente.get_nome())  # Mudança de nome do cliente
            cliente.set_endereco(cliente.get_endereco())  # Mudança de endereço do cliente
        else:
            print("Cliente inexistente!")

    def deletar(self, cpf: str):
        for cliente in self.clientes:  # Percorre a lista clientes
            if cliente.get_cpf() == cpf:  # Verifica se o cpf passado por parametro é igual a algum da lista clientes e se for:
                self.clientes.pop(self.clientes.index(
                    cliente))  # Chama o metodo pop para a lista clientes e passa por parametro o indice do numero do cpf pelo cliente
                print("Cliente deletado com sucesso!")
            else:
                print("Cliente não encontrado!")

    def listar(self):
        return self.clientes  # Retorna a lista clientes
