class Cliente:

    def __init__(self, cpf: str):
        self._cpf = cpf
        self._nome = str()
        self._endereco = str()

    def get_cpf(self):
        return self._cpf

    def set_cpf(self, cpf):
        self._cpf = cpf

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_endereco(self):
        return self._endereco

    def set_endereco(self, endereco):
        self._endereco = endereco

    def imprimircliente(self):
        return print("Cliente: {} | Endereço: {}". format(self._nome, self._endereco))

