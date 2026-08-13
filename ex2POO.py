## criando a Produto

class Produto:
    def __init__(self,codigo,nome,quantidade,preco_unitario):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def exibir_informacoes(self):
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Preço Unitário: R${self.preco_unitario:.2f}")

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

            if positivo_obrigatorio and numero <= 0:
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

        opcao = str(input("Escolha uma opção: "))

        # vereficador de opção de tela
        match opcao:

            case "1":
                print("=== Cadastro de Produto ===")

                codigo = validacao_universal("Digite o código do produto: ", int) #chama a função de validação universal para validar o código do produto

                nome = validacao_universal("Digite o nome do produto: ", str) #chama a função de validação universal para validar o nome do produto
                
                quantidade = 0 #crindo o obejto com a quantide padrão de 0

                preco_unitario = validacao_universal("Digite o preço unitário do produto: ", float) #chama a função de validação universal para validar o preço unitário do produto
                

                produto = Produto(codigo, nome, quantidade, preco_unitario)
                produtos.append(produto)
                print("Produto cadastrado com sucesso!")

            case "2":
                print("Listar Produtos")
                for i in range (len(produtos)):
                    print(f"\nO indice do produto é {i}")
                    print(produtos[i].exibir_informacoes)



            case "4":
                print("Saindo do programa...")
                break
menu() #inicia o programa chamando a função menu