notas = []
rodando = True
media = 0

while rodando:
    nota = int(input("Insira a nota: "))
    if(nota == -1):
        rodando = False
        break
    notas.append(nota)
    media += nota

media /= len(notas)
menor = min(notas)
maior = max(notas)

print("Média das notas: ", media)
print("Menor nota: ", menor)
print("Maior nota: ", maior)