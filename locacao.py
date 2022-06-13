from operacao import Operacao


class Locacao(Operacao):

    def __init__(self, periodo):
        super().__init__(self._cpf, self._codigo)
        self._periodo = periodo

    def get_periodo(self):
        return self._periodo

    def set_periodo(self, periodo):
        self._periodo = periodo