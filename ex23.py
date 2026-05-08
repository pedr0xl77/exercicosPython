import time
import sys

def carregar_sistema():
    print("Inicializando o sistema de gestão escolar", end="")
    for _ in range(3):
        time.sleep(0.5) # Espera meio segundo
        print(".", end="", flush=True) # O flush garante que o ponto apareça na hora
    print("\nSistema pronto!\n" + "="*30)

# Chame a função no início do seu programa
carregar_sistema()

def ClassificarAluno(nota):
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5 and nota < 7:
        return "Recuperação"
    else:
        return "Reprovado"

def MediaTurma(alunos):
    if not alunos:
        return 0
    
    total = 0
    for aluno in alunos:
        total += aluno["Nota"]
    return total / len(alunos)



alunos = []
total_aprovados = 0
total_reprovados = 0

while True:
    try:
        nome = input("Digite o nome do aluno: ").strip()
        if any(char.isdigit() for char in nome) or not nome:
            raise ValueError("Nome inválido! Não use números e não deixe vazio.")

        idade = int(input("Qual é a idade do aluno: "))
        if idade < 0:
            raise ValueError("A idade não pode ser negativa.")

        nota = int(input("Qual é a nota do aluno: "))
        if nota < 0 or nota > 10:
            raise ValueError("A nota deve ser entre 0 e 10.")

    except ValueError as e:
        print(f"Erro: {e}")
        continue 

    else:
        aluno = {"Nome": nome, "Idade": idade, "Nota": nota}
        alunos.append(aluno)
        print("Aluno cadastrado com sucesso!")

    try:
        opc = input("Deseja cadastrar outro aluno? (s/n): ").strip().lower()
        if opc not in ['s', 'n']:
            raise ValueError("Opção inválida! Digite 's' para sim ou 'n' para não.")
        
        if opc == 'n':
            break
    except ValueError as e:
        print(f"Erro: {e}")

print("Os alunos cadastrados são:")
for aluno in alunos:
    print(f"Nome: {aluno['Nome']}, Idade: {aluno['Idade']}, Nota: {aluno['Nota']}, Situação: {ClassificarAluno(aluno['Nota'])}\n")

print(f"A média da turma é: {MediaTurma(alunos):.2f}")

print("A quantidade de alunos aprovados é:")

for aluno in alunos:
    if ClassificarAluno(aluno['Nota']) == "Aprovado":
        total_aprovados += 1
print(total_aprovados)

print("A quantidade de alunos reprovados é:")
for aluno in alunos:
    if ClassificarAluno(aluno['Nota']) == "Reprovado":
        total_reprovados += 1
print(total_reprovados)

if alunos:
    maior_nota = max(aluno['Nota'] for aluno in alunos)
    menor_nota = min(aluno['Nota'] for aluno in alunos)

    for aluno in alunos:
        if aluno['Nota'] == maior_nota:
            print(f"Maior nota: {aluno['Nome']} ({aluno['Nota']})")
        if aluno['Nota'] == menor_nota:
            print(f"Menor nota: {aluno['Nome']} ({aluno['Nota']})")
