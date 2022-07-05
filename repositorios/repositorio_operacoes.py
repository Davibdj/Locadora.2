from Operacao.locacao import Locacao
from Operacao.operacao import Operacao
from Operacao.reserva import Reserva


class RepositorioOperacao:

    def __init__(self):
        self.operacoes = []  # Inicializa uma lista para operações

    def cadastrar(self, operacao: Operacao):
        for oper in self.operacoes:
            if self.buscar_reservas(oper.get_cpf()) is None:
                self.operacoes.append(oper)
                operacao.set_ativo(True)
            elif self.buscar_locacoes(oper.get_cpf()) is None:
                self.operacoes.append(oper)
                operacao.set_ativo(True)
        else:
            print("Reserva | Locação já presente no sistema! ")

    def buscar_reservas(self, cpf):
        reservas = []
        for ope in self.operacoes:
            if ope.get_cpf() == cpf:
                if ope.is_Ativo() is True:
                    if isinstance(ope, Reserva):
                        reservas.append(ope)
        return reservas

    def buscar_locacoes(self, cpf):
        locacoes = []
        for loc in self.operacoes:
            if loc.get_cpf() == cpf:
                if loc.is_Ativo() is True:
                    if isinstance(loc, Reserva):
                        locacoes.append(loc)
        return locacoes

    def deletar_reserva(self, cpf, codigo):
        for res in self.operacoes:
            if res.get_cpf() == cpf and res.get_codigo() == codigo and isinstance(res, Reserva):
                res.set_ativo(False)

    def deletar_locacao(self, cpf, codigo):
        for loc in self.operacoes:
            if loc.get_cpf() == cpf:
                if loc.get_codigo() == codigo:
                    if isinstance(loc, Locacao):
                        loc.set_ativo(False)

    def listar_locacoes(self, cpf):
        listoper = []
        for loc in self.operacoes:
            if loc.get_cpf() == cpf:
                if isinstance(loc, Operacao):
                    listoper.append(loc)
        return listoper

    def numero_locacoes_cpf(self, cpf):
        for ope in self.operacoes:
            if ope.get_cpf() == cpf:
                return len(self.operacoes)
        else:
            print("Cliente nâo encontrado")

    def numero_locacoes_codigo(self, codigo):
        for ope in self.operacoes:
            if ope.get_codigo() == codigo:
                return len(self.operacoes)
        else:
            print("Filme nâo encontrado")

    def numero_locacoes_ativas_cpf(self, cpf):
        for ope in self.operacoes:
            if ope.locacao.set_ativo() is True:
                if ope.get_cpf == cpf:
                    return len(ope.locacao.set_ativo() is True)
        else:
            print("Cliente não encontrado!")

    def numero_locacoes_ativas_codigo(self, codigo):
        for ope in self.operacoes:
            if ope.locacao.set_ativo() is True:
                if ope.get_codigo == codigo:
                    return len(ope.locacao.set_ativo() is True)
        else:
            print("Filme não encontrado!")

    def numero_reservas(self, codigo):
        for ope in self.operacoes:
            if ope.get_codigo() == codigo:
                if ope.is_Ativo() is True:
                    return len(self.operacoes)
        else:
            print("Filme nâo encontrado")


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
