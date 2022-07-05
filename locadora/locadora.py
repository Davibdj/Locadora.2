from Cliente.cliente import Cliente
from Filmes.filme import Filme
from repositorios.repositorio_clientes import RepositorioCliente
from repositorios.repositorio_filmes import RepositorioFilme
from repositorios.repositorio_operacoes import RepositorioOperacao


class Locadora:

    def __init__(self, clientes: RepositorioCliente, filmes: RepositorioFilme, operacoes: RepositorioOperacao):
        self._filmes = filmes
        self._clientes = clientes
        self._operacoes = operacoes

    def cadastrar(self, cliente: Cliente):
        self._clientes.cadastrar(cliente)

    def buscarcliente(self, cpf: str):
        self._clientes.buscar(cpf)

    def atualizarCadastro(self, cliente: Cliente):
        self._clientes.atualizar(cliente)

    def removerCliente(self, cpf: str):
        self._clientes.deletar(cpf)

    def cadastrarFilme(self, filme: Filme):
        self._filmes.cadastrar(filme)

    def atualizarCadastroFilme(self, filme: Filme):
        self._filmes.atualizar(filme)

    def removerFilme(self, codigo: int):
        self._filmes.deletar(codigo)

    def reservarFilme(self, cpf: str, codigo: int):
        pass

    def finalizarReservaFilme(self, cpf):
        pass

    def LocarFilme(self, cpf: str, codigo: int):
        pass

    def DevolverFilme(self, cpf: str, codigo: int):
        pass

    def ImprimirHistoricoLocacoes(self, cpf: str):
        pass

    def ImprimirFilmesMaisLocados(self, top: int):
        pass