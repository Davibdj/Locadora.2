from Filmes.filme import Filme

class RepositorioFilme:

    def __init__(self):
        self.filmes = [] #Inicializa uma lista

    def cadastrar(self, filme: Filme):
        if self.buscar(filme.get_codigo()) is None: #Procura um filme pelo metodo buscar com o codigo do filme e se ele não for nulo então:
            self.filmes.append(filme)               #Adiciona um filme a lista filmes
            print("Filme cadastrado com sucesso!")
        else:
            print("Filme já cadastrado.")

    def buscar(self, codigo):
        for filme in self.filmes:                  #
            if filme.get_codigo() == codigo:
                return filme
            else:
                return None

    def atualizar(self, filme):
        filme = self.buscar(filme.get_codigo())  # Procurando um cliente pelo metodo buscar(verifica o numero do cpf na lista cliente), pelo cpf e atribui a cliente
        if filme is not None:  # Se o cliente não for nulo então:
            filme.set_titulo(filme.get_titulo())
            filme.set_codigo(filme.get_codigo())
            filme.set_sinopse(filme.get_sinopse())
            filme.set_genero(filme.get_genero())
            filme.set_diretor(filme.get_diretor())
            filme.set_produtor(filme.get_produtor())
            filme.set_preco_locacao(filme.get_preco_locacao())
            filme.set_atores(filme.get_atores())
        else:
            print("Filme inexistente!")

    def deletar(self, codigo):
            for filme in self.filmes:
              if filme.get_codigo() == codigo:
               self.filmes.pop(self.filmes.index(filme))
               print("Filme deletado com sucesso!")
              else:
               print("Filme não encontrado!")

    def listar(self, filme):
        return self.filmes
