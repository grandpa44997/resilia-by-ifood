# Lendo as idades do teclado
minha_idade = int(input("Digite a sua idade: "))
idade_colega = int(input("Digite a idade do seu colega: "))

# Imprimindo os valores armazenados
print("Minha idade é:", minha_idade)
print("A idade do meu colega é:", idade_colega)

# Trocando os conteúdos entre as variáveis
minha_idade, idade_colega = idade_colega, minha_idade

# Imprimindo os valores armazenados após a troca
print("Minha idade agora é:", minha_idade)
print("A idade do meu colega agora é:", idade_colega)