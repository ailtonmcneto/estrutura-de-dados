#questão 2: Crie um programa que determine se um número inserido pelo usuário é par ou ímpar.
class Numeros:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def par(self):
        if self.numero1 % 2 == 0:
            print(f"{self.numero1} é par")
        else:
            print(f"{self.numero1} é ímpar")

        if self.numero2 % 2 == 0:
            print(f"{self.numero2} é par")
        else:
            print(f"{self.numero2} é ímpar")

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
Numeros1 = Numeros(numero1, numero2)
Numeros1.par()