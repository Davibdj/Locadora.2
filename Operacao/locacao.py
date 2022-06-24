from Operacao.operacao import Operacao


class Locacao(Operacao):

    def __init__(self, periodo: int):
        super().__init__(self._cpf, self._codigo)
        self._periodo = periodo

    def get_periodo(self):
        return self._periodo

    def set_periodo(self, periodo: int):
        self._periodo = periodo