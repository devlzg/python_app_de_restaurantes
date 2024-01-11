# pylint: disable=C0114
# pylint: disable=W0718
print('Exercício 1 e 2\n')
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in lista_numeros:
    print(num)
lista_nomes = ["Luiz", "João", "Gleyson", "Gabriel"]
for nome in lista_nomes:
    print(nome)
lista_ano = [2005, 2024]
for ano in lista_ano:
    print(ano)

print('Exercício 3\n')
IMPAR = 0
for i in lista_numeros:
    if i % 2 == 0:
        continue
    IMPAR += i
print(IMPAR)

print('Exercício 4\n')
for i in range(i - 1, -1, -1): # estudar sobre range depois
    print(lista_numeros[i])

print('Exercício 5\n')
numero_tabuada = int(input('Digite um número para ver a tabuada dele: '))
for i in lista_numeros:
    print(f'{numero_tabuada} X {i} = {numero_tabuada * i}')

print('Exercício 6\n')
lista_soma = [68, 54, 34, 31, 28, 25, 18, 15]
SOMA = 0
try:
    for num in lista_soma:
        SOMA += num
    print(SOMA)
except Exception as e:
    print(f'Ocorreu um erro: {e}')

print('Exercício 7\n')
try:
    SOMA = SOMA / len(lista_soma)
    print(SOMA)
except ZeroDivisionError:
    print('Impossível dividir por 0')
except Exception as e:
    print(f'Ocorreu um erro: {e}')
