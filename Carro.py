class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        return f"Carro: {self.marca} {self.modelo} ({self.ano})"


if __name__ == "__main__":
    carro = Carro("Toyota", "Corolla", 2022)
    print(carro.detalhes())
