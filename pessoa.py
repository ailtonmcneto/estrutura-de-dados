class Pessoa:
  def __init__(self,nome):
    self.nome = nome


  def cumprimentar(self):
    print(f"Olá, {self.nome}")

nome = input("Digite seu nome: ")
Pessoa1 = Pessoa(nome)
Pessoa1.cumprimentar()
