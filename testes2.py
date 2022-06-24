from Cliente.cliente import Cliente
from Filmes.filme import Filme
from repositorios.repositorio_clientes import RepositorioCliente
from repositorios.repositorio_filmes import RepositorioFilme


class Testes:
    #Teste classe filme

    if __name__ == '__main__':
         filme = Filme(658, "Call me by Your Name")
         filme.set_genero(["Romance", "LGBT"])
         filme.set_diretor(["André Aciman"])
         filme.set_atores(["Timothe"])
         filme.imprimir()



    #Teste classe cliente

    if __name__ == '__main__':
         cliente = Cliente('06898569856')
         cliente.set_nome(["Davi"])
         cliente.set_endereco(["Travessa Jurandir Bastos, nº56"])
         cliente.imprimircliente()



    #Teste repositorio cliente

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


    #Teste repositorio filmes

    if __name__ == '__main__':
        filme = Filme(658, "Call me by Your Name")
        filme.set_genero(["Romance", "LGBT"])
        filme.set_diretor(["André Aciman"])
        filme.set_atores(["Timothe"])
        filme.imprimir()

        repoFilme = RepositorioFilme()
        repoFilme.cadastrar(filme)