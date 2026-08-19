#questão 4
numeros = []
while True:
    try:
        numero = int(input("Digite um número para adicionar na lista: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue
    numeros.append(numero)
    continuar = input("Deseja adicionar outro número? (s/n): ")
    if continuar.lower() != 's':
        break
    else:
        continue
print("maior numero da lista é:", max(numeros))
print("menor numero da lista é:", min(numeros))