### Exercícios de Programação Orientada a Objetos (POO)

Todos os exercícios referentes à matéria de POO possuem o prefixo **POO** no nome do arquivo. Os demais arquivos presentes no repositório pertencem a atividades antigas. 

### Descrição do Exercício: Ex2POO.py

O arquivo Ex2POO.py foi desenvolvido utilizando os conceitos de POO e boas práticas de reaproveitamento de código. Abaixo está a explicação detalhada da estrutura da solução: 

### 1. Estrutura da Classe

* **Atributos:** A classe possui dois atributos principais: nome e preco_unitario.
* **Métodos:** Contém o método exibir_informacoes(), responsável por exibir os dados do produto.

### 2. Otimização de Entrada de Dados (Inputs)

Durante o desenvolvimento, notei uma alta repetição de código na leitura dos dados. Para solucionar isso, criei uma função de validação universal que recebe a mensagem a ser exibida e o tipo de dado esperado. Ela opera sob as seguintes regras: 

* **Validação de Strings:** Garante que o campo não seja deixado em branco e impede que a resposta contenha exclusivamente números.
* **Validação de Números (int e float):** Impede a inserção de valores negativos.
* **Flexibilidade de Formatação:** Permite que o usuário digite números decimais utilizando vírgula, convertendo-os automaticamente para ponto no sistema.
* **Parâmetro Opcional:** Caso o campo aceite o número zero como valor válido, basta passar o parâmetro positivo_obrigatorio = False ao chamar a função.

### 3. Menu de Navegação

O fluxo principal do programa é gerenciado por um laço de repetição (loop) integrado a uma estrutura de seleção match case (o *switch case* do Python), contendo quatro opções: 

* **Opção 1:** Solicita o nome e o preço unitário, instancia um objeto da classe Produto e o adiciona a uma lista de produtos.
* **Opção 2:** Identifica os itens armazenados na lista e chama o método exibir_informacoes() de cada objeto.
* **Opção 3:** Solicita o índice do produto desejado e a quantidade de compra. O sistema realiza o cálculo final com base no preço unitário correspondente.
* **Opção 4:** Encerra a execução do menu e finaliza o programa.
