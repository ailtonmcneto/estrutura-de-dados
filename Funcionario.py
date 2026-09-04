class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, percentual):
        self.salario += self.salario * (percentual / 100)
        return self.salario


if __name__ == "__main__":
    funcionario = Funcionario("Ana", 3000, "Analista")
    funcionario.aumentar_salario(10)
    print("Novo salário de", funcionario.nome, ":", funcionario.salario)
