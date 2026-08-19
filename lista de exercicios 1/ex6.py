#questão 6
fatorial = 1
numero = int(input("Digite um número que quer saber o fatorial: ")) 
for i in range(1, numero + 1):
    fatorial *= i
for i in range(1, numero + 1):
    print(f"{i} x " if i < numero else f"{i} = {fatorial}", end="")