from Operacao import operacao
from Operacao.operacao import Operacao
from Operacao.reserva import Reserva


class RepositorioOperacoes:

    def __init__(self):
        self.operacoes = []  # Inicializa uma lista para operações

    def cadastrar(self, operacao: Operacao):
        for oper in self.operacoes:
            if self.buscar_reservas(operacao.get_cpf()) is None:
                self.operacoes.append(oper)
                operacao.set_ativo(True)
            elif self.buscar_locacoes(operacao.get_cpf()) is None:
                self.operacoes.append(oper)
                operacao.set_ativo(True)
        else:
            print("Reserva | Locação já presente no sistema! ")

    def buscar_reservas(self, cpf):
        reservas = []
        for ope in self.operacoes:
            if ope.get_cpf() == cpf:
                if ope.Is_Ativo(True):
                    if isinstance(ope, Reserva):
                        reservas.append(ope)
            else:
                print("Reserva não encontrada!")
        return reservas

    def buscar_locacoes(self, cpf):
        locacoes = []
        for loc in self.operacoes:
            if loc.get_cpf() == cpf:
                if loc.Is_Ativo(True):
                    if isinstance(loc, Reserva):
                        locacoes.append(loc)
            else:
                print("Locação não encontrada!")
        return locacoes

    def deletar_reserva(self, cpf, codigo):
        for res in self.operacoes:
            if operacao.get_cpf() == cpf and operacao.get_cpf():
                pass

    def deletar_locacao(self, cpf, codigo):
        pass

    def listar_locacoes(self, cpf):

        for res in self.operacoes:
            if res.get_cpf() == cpf:
                return self.operacoes
            else:
                return None

    def numero_locacoes_cpf(self, cpf):
        pass

    def numero_locacoes_codigo(self, codigo):
        pass

    def numero_locacoes_ativas_cpf(self, cpf):
        o = 0
        for i in self.operacoes:
            if self.buscar_locacoes(Operacao.get_cpf()) == cpf:
                pass

    def numero_locacoes_ativas_codigo(self, codigo):
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
