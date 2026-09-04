class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"Olá, meu nome é {self.nome}.")


if __name__ == "__main__":
    pessoa = Pessoa("Maria", 25)
    pessoa.falar()
