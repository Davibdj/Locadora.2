
class Locadora:

    def __init__(self, RepositorioFilme, RepositorioCliente, RepositorioOperacao):
        self._filmes = RepositorioFilme
        self._clientes = RepositorioCliente
        self._operacoes = RepositorioOperacao

    def cadastrar(self):