#questão 1: Faça um programa que calcule a média de três números inseridos pelo usuário.
class Numeros:
    def __init__(self, numero1, numero2, numero3):
        self.numero1 = numero1
        self.numero2 = numero2
        self.numero3 = numero3

    def media(self):
        media = (self.numero1 + self.numero2 + self.numero3) / 3
        return media


numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o segundo numero: "))
numero3 = int(input("digite o terceiro numero: "))

Numeros1 = Numeros(numero1, numero2, numero3)
print("A média dos números é: ", Numeros1.media())


