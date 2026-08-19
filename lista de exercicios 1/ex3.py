#questão 3
class Numeros:
    def __init__(self, numero1):
        self.numero1 = numero1

    def numerosPares(self):
        if self.numero1 <=0 or self.numero1 == 1:
            print("Digite um número maior que 0 e 1")
        else:            
            print("numeros pares de 0 até", self.numero1, ":")
            for i in range(2,self.numero1 +1,2):
                print(i)
                
numero1 = int(input("Digite um número: ")) 
Numeros1 = Numeros(numero1)
  
Numeros1.numerosPares()