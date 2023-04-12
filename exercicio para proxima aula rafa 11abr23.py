# Definindo as duas funções que serão utilizadas
def expressao1(a, b, c, d):
    resultado = a*c - b*d
    return resultado

def expressao2(a, b, c, d):
    resultado = (a + b + c + d)/4
    return resultado

# Lendo os quatro números de entrada
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
d = float(input("Digite o valor de d: "))

# Chamando as funções e armazenando os resultados em variáveis
resultado1 = expressao1(a, b, c, d)
resultado2 = expressao2(a, b, c, d)

# Exibindo os resultados na tela
print("O resultado da expressão 1 é:", resultado1)
print("O resultado da expressão 2 é:", resultado2)
