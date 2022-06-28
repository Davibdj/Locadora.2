from Operacao import operacao
from Operacao.operacao import Operacao
from Operacao.reserva import Reserva


class Repositorio_Operacoes():

    def __init__(self):
        self.operacoes = []

    def cadastrar(self, operacao: Operacao):
        if self.buscar_reservas(operacao.get_cpf()) is None:
            self.operacoes.append(operacao)
        elif self.buscar_locacoes(operacao.get_cpf()) is None:
            self.operacoes.append(operacao)

        else:
            print("Reserva| Locação Encontradas")

    def buscar_reservas(self, cpf):
        pass

    def buscar_locacoes(self, cpf):
        pass

    def deletar_reserva(self, cpf, codigo):
        pass

    def deletar_locacao(self, cpf, codigo):
        pass

    def listar_locacoes(self, cpf):
        pass

    def numero_locacoes_cpf(self, cpf):
        pass

    def numero_locacoes_codigo(self, codigo):
        pass

    def numero_locacoes_ativascodigo(self, cpf):
        pass

    def numero_locacoes_ativascpf(self, codigo):
        pass

    def numero_reservas(self, codigo):
        pass



'''
 reservas = []
        for operacao in self.operacao:
           if operacao.get_cpf() == cpf:
             if operacao.Is_Ativo() == True:
               if isinstance(operacao, Reserva):
                 return reservas
           else:
                print("Reserva não encontrada!")

'''


