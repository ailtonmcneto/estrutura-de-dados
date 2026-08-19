import pessoa

nome = str(input("digite o nome: "))
idade = int(input("digite a idade: "))

pessoa1 = pessoa.pessoa(nome, idade)
pessoa1.apresentar()