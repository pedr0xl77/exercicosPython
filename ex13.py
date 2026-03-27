nomes = []
idades = []
rodando = True

print('Digite "encerrar" no campo de nome caso queira finalizar o programa.')
while rodando:
    nome = input("Qual o seu nome: ")
    if(nome.lower() == "encerrar"):
        rodando = False
        break
    idade = int(input("Qual sua idade: "))
    
    nomes.append(nome)
    idades.append(idade)

qtde = len(nomes)
print("A quantidade de usuários é: ",qtde)

usuariosMaiores = 0
for i in range(0, qtde):
    if idades[i] >= 18:
        usuariosMaiores += 1
        
print(usuariosMaiores, " usuários sâo maiores de 18 anos")