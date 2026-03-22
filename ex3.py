codProd = int(input("Digite o código do produto: "))
valorProd = float(input("Digite o valor do produto: "))
qtd = int(input("Digite a quantidade do produto: "))
codigoVendedor = int(input("Digite o código do vendedor: "))

print("O vendedor ", codigoVendedor, " vendeu o produto ", codProd, " no valor total de R$ ", valorProd * qtd, " na quantidade de ", qtd, "e teve uma comissa de : R$ ", (valorProd * qtd) * 0.05)