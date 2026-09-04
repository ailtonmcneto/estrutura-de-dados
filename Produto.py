class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade


if __name__ == "__main__":
    produto = Produto("Caneta", 2.50, 10)
    print("Valor total:", produto.calcular_total())
