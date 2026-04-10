def conta(valor,qtd):
    total = qtd * valor
    return total

num1 = float(input("Qual é o valor do produto: "))
num2 = int(input("Qual é a quantidade vendida"))

print(conta(num1,num2))