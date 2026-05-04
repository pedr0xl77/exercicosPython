try:
    valor = int(input("Digite o valor do produto: "))
    qtd = float(input("Digite a quantidade: "))
    total = valor * qtd
    print(f"O valor total da compra é: R${total:.2f}")
except ValueError:
    print("Valor inválido. Por favor, digite números inteiros.")