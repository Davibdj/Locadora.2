import random
from datetime import date


class Filme:

    def __init__(self, codigo: int, titulo: str):
        self._codigo = codigo
        self._titulo = titulo
        self._genero = list()
        self._data_lancamento = date.today()
        self._diretor = str
        self._atores = list()
        self._sinopse = str
        self._produtores = list()
        self._preco_alocacao = float()
        self._numero_copias = int()

    def get_codigo(self):
        return self._codigo

    def set_codigo(self, codigo: int):
        self._codigo = codigo

    def get_titulo(self):
        return self._titulo

    def set_titulo(self, titulo: str):
        self._titulo = titulo

    def get_genero(self):
        return self._genero

    def set_genero(self, genero: list):
        self._genero = genero

    def addGenero(self, genero):
        self._genero += genero

    def get_data_lancamento(self):
        return self._data_lancamento

    def set_data_lancamento(self, data_lancamento: date):
        self._data_lancamento = data_lancamento

    def get_diretor(self):
        return self._diretor

    def set_diretor(self, diretor: str):
        self._diretor = diretor

    def get_atores(self):
        return self._atores

    def set_atores(self, atores: list):
        self._atores = atores

    def addAtores(self, ator):
        self._atores += ator

    def get_sinopse(self):
        return self._sinopse

    def set_sinopse(self, sinopse: str):
        self._sinopse = sinopse

    def get_produtores(self):
        return self._produtores

    def set_produtores(self, produtores: list):
        self._produtores = produtores

    def addProdutor(self, produtor):
        self._produtores += produtor

    def get_precoalocacao(self):
        return self._preco_alocacao

    def set_precoalocacao(self, preco_alocacao: float):
        self._preco_alocacao = preco_alocacao

    def get_numerocopias(self):
        return self._numero_copias

    def set_numerocopias(self, numero_copias: int):
        self._numero_copias = numero_copias

    def imprimir(self):
        return print(
            "Titulo: {} | Código: {} | Gênero: {} | Data de lançamento: {} | Diretor: {} | Atores: {} | Sinopse: {}  ".format(self._titulo, self._codigo, self._genero, self._data_lancamento, self._data_lancamento, self._diretor,self._atores, self._sinopse))
