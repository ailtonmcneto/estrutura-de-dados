class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)


if __name__ == "__main__":
    aluno = Aluno("Pedro", [8.0, 7.5, 9.0])
    print("Média de", aluno.nome, ":", aluno.calcular_media())
