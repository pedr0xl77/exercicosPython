nome = input("Qual é o seu nome? ")
salario = float(input("Qual é o seu salário? "))

salarioNovo = 0
if salario <=1000:
    salarioNovo = salario * 1.20
elif salario <= 5000:
    salarioNovo = salario * 1.10
else:
    salarioNovo = salario * 1.05

print("O novo salário do ", nome, " é: R$ ", salarioNovo)