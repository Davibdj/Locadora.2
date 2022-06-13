from filme import Filme

class Repositorio_Filme:

    def __init__(self):
        self.filmes = []

    def cadastrar(self, filme: Filme):
        self.filmes.append(filme)

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