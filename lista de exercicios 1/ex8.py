numero = int(input("Digite um número: "))
if numero < 2:
    e_primo=False
 
for divisor in range(2, numero):
    if numero % divisor == 0:
        e_primo = False
        break
    else:
        e_primo = True

if e_primo:
    print(f"{numero} é primo")
else:
    print(f"{numero} não é primo")
