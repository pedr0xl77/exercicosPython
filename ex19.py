aluno = {}

aluno["nome"] = input("Digite o nome do aluno: ")
aluno["idade"] = int(input("Digite a idade do aluno: "))
aluno["nomeMae"] = input("Digite o nome da mãe do aluno: ")

print("Dados do aluno: ")

for chave,valor in aluno.items():
    print(f"{chave}: {valor}")