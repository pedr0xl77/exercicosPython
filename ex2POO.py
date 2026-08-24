## criando a Produto

class Produto:
    def __init__(self,nome,preco_unitario):
        self.nome = nome
        self.preco_unitario = preco_unitario

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Preço Unitário: R${self.preco_unitario:.2f}".replace('.', ','))

#Função de validação universal para entrada de dados
def validacao_universal(mensagem, tipo_esperado, positivo_obrigatorio=True):
    while True:
        try:
            entrada = input(mensagem).strip()

            #validação universal para verificar se o campo está vazio
            if not entrada:
                print("Erro: O campo não pode ser vazio.")
                continue

            #validação para texto
            if tipo_esperado == str:
                if not any(c.isalpha() for c in entrada):
                    raise ValueError("O texto deve conter letras.")
                return entrada

            #troca de , por . para permitir a entrada de números decimais
            if tipo_esperado == float:
                entrada = entrada.replace(",", ".")
            #validação para números
            numero = tipo_esperado(entrada)

            if positivo_obrigatorio == True and numero <= 0:
                raise ValueError("O número deve ser maior que zero.")

            return numero
        except ValueError:
            if tipo_esperado == str:
                print("Erro: O texto deve conter letras.")
            elif tipo_esperado == int:
                print("Erro: Deve ser um numero inteiro maior que zero.")
            else:
                print("Erro: Deve ser um numero decimal maior que zero.")







# Função para exibir o menu e interagir com o usuário
def menu():
    produtos = []  # Lista para armazenar os produtos cadastrados
    while True:
        print("=== Menu ===")
        print("1. Cadastrar produto")
        print("2. Listar produtos")
        print("3. Comprar produtos")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        # vereficador de opção de tela
        match opcao:

            case "1":
                while True:
                    print("=== Cadastro de Produto ===")
                    
                    nome = validacao_universal("Digite o nome do produto: ", str) #chama a função de validação universal para validar o nome do produto
                                    
                    preco_unitario = validacao_universal("Digite o preço unitário do produto: ", float) #chama a função de validação universal para validar o preço unitário do produto
                                    
                    
                    produto = Produto(nome, preco_unitario)
                    produtos.append(produto)
                    print("Produto cadastrado com sucesso!")
                    alternativa = validacao_universal("Deseja continuar? S|N",str).upper()
                    if alternativa == "S":
                        continue
                    else:
                        break
                        

            case "2":
                print("Listar Produtos")
                for i in range (len(produtos)):
                    print(f"\nO indice do produto é {i}")
                    produtos[i].exibir_informacoes()

            case "3":
                print("Comprar Produtos")
                if not produtos:
                    print("Nenhum produto cadastrado.")
                    continue

                indice = validacao_universal("Digite o índice do produto que deseja comprar: ", int, positivo_obrigatorio=False)
                if indice < 0 or indice >= len(produtos):
                    print("Índice inválido.")
                    continue
                
                quantidade = validacao_universal("Digite a quantidade de produtos que deseja comprar: ", int)
                total = 0

                total = produtos[indice].preco_unitario * quantidade
                print(f"Total da compra: R${total:.2f}".replace('.', ','))
                print(f"Voce comprou {quantidade} unidades do produto {produtos[indice].nome}.")
                print("Compra realizada com sucesso!")


            case "4":
                print("Saindo do programa...")
                break
menu() #inicia o programa chamando a função menu