class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        return f"Livro: {self.titulo} - Autor: {self.autor}"


if __name__ == "__main__":
    livro = Livro("Dom Casmurro", "Machado de Assis")
    print(livro.detalhes())
