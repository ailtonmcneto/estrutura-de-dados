class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


if __name__ == "__main__":
    retangulo = Retangulo(4, 6)
    print("Área do retângulo:", retangulo.calcular_area())
