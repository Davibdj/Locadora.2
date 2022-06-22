from repositorios.repositorio_clientes import RepositorioCliente
from Filmes.filme import Filme
from Cliente.cliente import Cliente
from repositorios.repositorio_filmes import RepositorioFilme

'''
class Criarfilme:
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

'''
class TesteRepoCliente:
    if __name__ == '__main__':
        cliente = Cliente('06898569856')
        cliente_1 = Cliente('06898569856')
        cliente.set_nome(["Davi"])
        cliente.set_endereco(["Travessa Jurandir Bastos, nº56"])

        repoCliente = RepositorioCliente()
        repoCliente.cadastrar(cliente)
        repoCliente.cadastrar(cliente_1)

        cliente.imprimircliente()

        cliente.set_nome(["Wanderson"])
        repoCliente.atualizar(cliente)

        for cl in repoCliente.listar():
            cl.imprimircliente()

        cliente.set_endereco(["Monte castelo"])
        repoCliente.atualizar(cliente)

        for c in repoCliente.listar():
            c.imprimircliente()

'''
class TesteRepoFilmes:

    if __name__ == '__main__':
        filme = Filme(658, "Call me by Your Name")
        filme.set_genero(["Romance", "LGBT"])
        filme.set_diretor(["André Aciman"])
        filme.set_atores(["Timothe"])
        filme.imprimir()

        repoFilme = RepositorioFilme()
        repoFilme.cadastrar(filme)
'''



