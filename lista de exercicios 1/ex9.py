#questão 9
nomes = []
nomesA = []
while True:
    nome = input("Digite um nome para adicionar na lista: ")
    nomes.append(nome)
    continuar = input("Deseja adicionar outro nome? (s/n): ")
    if continuar.lower() != 's':
        break
    else:
        continue

for nome in nomes:
    if nome[0].lower() == 'a':
        nomesA.append(nome)

if len(nomesA) == 0:
    print("Não há nomes que comecem com a letra 'A' na lista.")
else:
    print("Nomes que começam com a letra 'A':")
    for nome in nomesA:
        print(nome)
