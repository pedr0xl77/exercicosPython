try:
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    resultado = valor1 + valor2
    print(f"O resultado da soma é: {resultado}")
except ValueError:
    print("Valor inválido. Por favor, digite números inteiros.")