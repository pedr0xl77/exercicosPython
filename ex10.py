nota1 = float(input("qual é a primeira nota: "))
nota2 = float(input("qual é a segunda nota: "))
nota3 = float(input("qual é a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 8:
    print("sua média é ",media," e vc ficou com A")
elif media >= 5:
    print("sua média é ",media," e vc ficou com B")
else:
    print("sua média é ",media," e vc ficou com c")