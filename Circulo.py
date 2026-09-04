class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14159 * self.raio ** 2


if __name__ == "__main__":
    circulo = Circulo(5)
    print("Área do círculo:", circulo.calcular_area())
