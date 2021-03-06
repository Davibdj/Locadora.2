from Operacao.operacao import Operacao


class Reserva(Operacao):

    def __init__(self, prioridade: int):
        super().__init__(self._cpf, self._codigo)
        self._prioridade = prioridade

    def get_prioridade(self):
        return self._prioridade

    def set_prioridade(self, prioridade: int):
        self._prioridade = prioridade
