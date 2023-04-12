# Solicita que o usuário digite um número inteiro
Numero = int(input("Digite um número inteiro: "))

# Verifica se o número é um múltiplo de 5, calculando o resto da divisão por 5
# Se o resto for zero, significa que o número é divisível por 5
if Numero % 5 == 0:
    # Se a condição acima for verdadeira, imprime uma mensagem informando que o número é um múltiplo de 5
    print(Numero, "é um múltiplo de 5")
else:
    # Se a condição acima for falsa, imprime uma mensagem informando que o número não é um múltiplo de 5
    print(Numero, "não é um múltiplo de 5")
