def vereficador(num):
    if num > 18:
        mensagem = "é de maior"
    else:
        mensagem = "é de menor"
    return mensagem

idade = int(input("Qual é sua idade "))
print(vereficador(idade))