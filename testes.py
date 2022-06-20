
from Filmes.filme import Filme
from Cliente.cliente import Cliente
from Operacao.operacao import Operacao

class criarfilme:

    if __name__ == '__main__':
        filme = Filme(658, "Call me by Your Name")
        filme.set_genero(["Romance", "LGBT"])
        filme.set_diretor(["André Aciman"])
        filme.set_atores(["Timothe"])
        filme.imprimir()

class criarCliente:

    if __name__ == '__main__':
        cliente = Cliente('06898569856')
        cliente.set_nome(["Davi"])
        cliente.set_endereco(["Travessa Jurandir Bastos, nº56"])
        cliente.imprimircliente()


