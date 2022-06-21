from Filmes.filme import Filme

class RepositorioFilme:

    def __init__(self):
        self.filmes = []


    def cadastrar(self, filme: Filme):
        if self.buscar(filme.get_codigo()) is None:
            self.filmes.append(filme)
            print("Filme cadastrado com sucesso!")
        else:
            print("Filme já cadastrado.")


    def buscar(self, codigo):
        for filme in self.filmes:
            if filme.get_codigo() == codigo:
                return filme
            else:
                return None

    def atualizar(self, filme):
        pass

    def deletar(self, codigo):
       pass

    def listar(self, filme):
        pass