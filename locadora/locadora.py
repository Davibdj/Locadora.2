from Cliente.cliente import Cliente
from Filmes.filme import Filme
from repositorios.repositorio_clientes import RepositorioCliente
from repositorios.repositorio_filmes import RepositorioFilme
from repositorios.repositorio_operacoes import RepositorioOperacao


class Locadora:

    def __init__(self, clientes: RepositorioCliente, filmes: RepositorioFilme, operacoes: RepositorioOperacao):
        self._filmes = RepositorioFilme
        self._clientes = RepositorioCliente
        self._operacoes = RepositorioOperacao

    def cadastrar(self, cliente: Cliente):
        pass

    def buscarcliente(self, cpf: str):
        pass

    def atualizarCadastro(self, cliente: Cliente):
        pass

    def removerCliente(self, cpf: str):
        pass

    def cadastrarFilme(self, filme: Filme):
        pass

    def atualizarCadastroFilme(self, filme: Filme):
        pass

    def removerFilme(self, codigo: int):
        pass

    def reservarFilme(self, cpf: str, codigo: int):
        pass

    def finalizarReservaFilme(self, cpf):