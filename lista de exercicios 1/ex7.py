#questão 7
a = 0
b = 1 
numero = int(input("Digite um número que queira ver a sequência de Fibonacci: "))
while True:
    if  a > numero:
        break
    else:
       print(a, end=" ")
    a, b = b, a + b