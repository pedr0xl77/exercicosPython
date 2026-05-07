alunos = []

def cadastrarAluno():
    while True:
        try:
            nome = input("digite o nome do aluno: ")
            idade = int(input("Qual é a idade do aluno: "))
            nota = int(input("qual é a nota do aluno: "))
        except ValueError:
            print("O valor digitado é invalido")
        else:
            print("Aluno cadastrado com sucesso")
            aluno = {"Nome":nome,"Idade":idade,"Nota":nota}
            alunos.append(aluno)
            break


cadastrarAluno()