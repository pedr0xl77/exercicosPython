# 1- Crie uma classe chamada produto, com os atributos código, nome, 
# quantidade e preço unitário. Crie um objeto para a classe 
# produto e mostre seus dados, e crie um método que mostre as informações do produto

class Produto:
    def __init__(self, cod, nome, qtd, preco):
        self.cod = cod
        self.nome = nome
        self.qtd = qtd
        self.preco = preco

    def mostrar (self):
        print(f"Código: {self.cod}\nNome: {self.nome}\nQuantidade: {self.qtd}\nPreço: R${self.preco}\n")

prod1= Produto (2091114,"Pente", 3, 30 )
prod1.mostrar()