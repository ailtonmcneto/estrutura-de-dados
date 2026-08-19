#questão 5
numeros = []
pares = []
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
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
if len(pares) == 0:
    print("Não há números pares na lista.")
else:
    media = sum(pares) / len(pares)
    print(f"A média dos números pares é: {media}") 
