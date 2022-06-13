from datetime import date

class Operacao:

    def __init__(self, cpf, codigo_operacao):
        self._codigo_operacao = codigo_operacao
        self._cpf = cpf
        self._dataoperacao = date
        self._ativo = bool()

    def get_codigo_operacao(self):
        return self._codigo_operacao

    def set_codigo_operacao(self, codigo_operacao):
        self._codigo_operacao = codigo_operacao

    def get_cpf(self):
        return self._cpf

    def set_cpf(self, cpf):
        self._cpf = cpf

    def get_dataoperacao(self):
        return self._dataoperacao

    def set_dataoperacao(self, dataoperacao):
        self._dataoperacao = dataoperacao

    def get_ativo(self):
        return self._ativo

    def set_ativo(self, ativo):
        self._ativo = ativo


