
from Filmes.filme import Filme

class criarfilme:

    if __name__ == '__main__':
        filme = Filme(658, "Call me by Your Name")
        filme.set_genero(["Romance", "LGBT"])
        filme.set_diretor(["André Aciman"])
        filme.set_atores(["Timothe"])
        filme.imprimir()

