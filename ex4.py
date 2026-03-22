PrecoVeiculo = float(input("Digite o preço do veículo: "))

imposto = PrecoVeiculo * 0.45
lucro = PrecoVeiculo * 0.28
precoFinal = PrecoVeiculo + imposto + lucro

print("O preço do veiculo é: R$ ", PrecoVeiculo)
print("O valor do imposto é: R$ ", imposto)
print("O valor do lucro é: R$ ", lucro)
print("O preço final do veículo é: R$ ", precoFinal)