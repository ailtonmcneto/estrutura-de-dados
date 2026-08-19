from unittest import case


class Calculadora:
  def __init__(self,a,b):
    self.a = a
    self.b = b

def subtracao(self):
   self.a - self.b

def multiplicacao(self):
  self.a * self.b

def divisao(self):
  self.a / self.b

def soma(self):
  self.a + self.b

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

while True:
  x = int(input("""Digite a operação que deseja realizar:
  1 - soma
  2 - subtração
  3 - multiplicação
  4- divisão"""))

  match x:
    case 1:
        Calculadora.soma()
        break
    case 2:
        Calculadora.subtracao()
        break
    case 3:
        Calculadora.multiplicacao()
        break
    case 4:
        Calculadora.divisao()
        break
    case _:
        print("Selecione uma opção válida")


