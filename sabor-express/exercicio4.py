"""04. Dicionários"""
# pylint: disable=C0103
# Exercício 1
dados_pessoais = {'nome': 'Giovanna Regina Brito de Farias',
                  'idade': 19, 'cidade': 'Lúcio Costa'}
print(dados_pessoais)

# Exercício 2
dados_pessoais['cidade'] = 'Valparaíso'
print(dados_pessoais)

dados_pessoais['profissao'] = 'Estudante'
print(dados_pessoais)

# del é usado para remover uma chave e seu valor de um dicionário
del dados_pessoais['idade']
print(dados_pessoais)

# Exercício 3
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

# Exercício 4
if 'profissao' in dados_pessoais:
    print('O dado foi encontrado!')
else:
    print('O dado não foi encontrado!')

# Exercício 5
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_de_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_de_palavras[palavra] = contagem_de_palavras.get(palavra, 0) + 1
print(contagem_de_palavras)
