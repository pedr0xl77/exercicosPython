nome = input("Digite o seu nome de usuário: ")
senha = "adm@123"
for i in range(1, 4):
    senhaDigitada = input("Insira a senha: ")
    if senhaDigitada == senha:
        print("Acesso permitido.")
        break
    else:
        print("Senha incorreta")
        if i == 3:
            print("Conta bloqueada")