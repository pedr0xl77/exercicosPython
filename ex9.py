peso = float(input("Digite o seu peso: "))
altura = float(input("digite a sua altura em metros: "))

imc = peso / (altura ** 2)
print("Seu IMC é ",imc)
if imc < 18.5:
    print("Você está abaixo do peso ideal")
elif imc < 25:
    print("Você está no peso ideal")
elif imc < 30:
    print("Você está acima do peso ideal")
elif imc < 35:
    print("Você está no grau de obesidade 1")
elif imc < 40:
    print("Você está no grau de obesidade 2")
else:
    print("Você está no grau de obesidade 3")