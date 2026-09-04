class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")
        return self.saldo


if __name__ == "__main__":
    conta = ContaBancaria("João", 100)
    conta.depositar(50)
    conta.sacar(30)
    print("Saldo de", conta.titular, ":", conta.saldo)
