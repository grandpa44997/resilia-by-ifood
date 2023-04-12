# Pede ao usuário que digite o valor do produto e armazena esse valor em uma variável chamada "ValorProduto"
ValorProduto = float(input("Digite o valor do produto: "))

# Verifica se o valor do produto é menor que R$ 20,00. Se for, armazena o valor 0,45 (45% de lucro) na variável "MargemLucro".
# Se não for, armazena o valor 0,3 (30% de lucro) na mesma variável.
if ValorProduto < 20:
    MargemLucro = 0.45
else:
    MargemLucro = 0.3

# Calcula o valor de venda do produto, multiplicando o valor do produto pela margem de lucro mais 1 (para incluir o valor do produto na venda)
ValorVenda = ValorProduto * (1 + MargemLucro)

# Imprime na tela o valor de venda do produto formatado com duas casas decimais
print("O valor de venda do produto é R$ {:.2f}.".format(ValorVenda))
