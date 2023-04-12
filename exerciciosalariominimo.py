# Definindo o valor do salário mínimo
SalarioMinimo = 1302

# Pedindo que o usuário informe o seu salário
salario = float(input("Digite o valor do seu salário: "))

# Realizando o cálculo para obter quantos salários mínimos o usuário recebe
QuantidadeSalariosMinimos = salario / SalarioMinimo

# Imprimindo a quantidade de salários mínimos recebidos
print(f"O seu salário é equivalente a {QuantidadeSalariosMinimos:.2f} salários mínimos.")