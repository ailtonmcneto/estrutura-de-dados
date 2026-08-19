class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"olá, meu nome é {self.nome} e tenho {self.idade} anos")