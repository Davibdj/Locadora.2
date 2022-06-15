from datetime import date


class Operacao:

    def __init__(self, cpf: str, codigo: int):
        self._codigo = codigo
        self._cpf = cpf
        self._dataoperacao = date.today()
        self._ativo = bool()

    def get_codigo(self):
        return self._codigo

    def set_codigo(self, codigo):
        self._codigo = codigo

    def get_cpf(self):
        return self._cpf

    def set_cpf(self, cpf):
        self._cpf = cpf

    def get_dataoperacao(self):
        return self._dataoperacao

    def set_dataoperacao(self, dataoperacao):
        self._dataoperacao = dataoperacao

    def isAtivo(self):
        return self._ativo
