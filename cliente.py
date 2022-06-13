class Cliente:

    def __init__(self, cpf, nomecliente, enderecocliente):
        self._cpf = cpf
        self._nomecliente = nomecliente
        self._enderecocliente = enderecocliente

    def get_cpf(self):
        return self._cpf

    def set_cpf(self, cpf):
        self._cpf = cpf

    def get_nomecliente(self):
        return self._nomecliente

    def set_nomecliente(self, nomecliente):
        self._nomecliente = nomecliente

    def get_enderecocliente(self):
        return self._enderecocliente

    def set_enderecocliente(self, enderecocliente):
        self._enderecocliente = enderecocliente

    def imprimircliente(self):
        return print("Cliente: {} | CPF: {} | Endereço: {}". format(self._nomecliente, self._cpf, self._enderecocliente))