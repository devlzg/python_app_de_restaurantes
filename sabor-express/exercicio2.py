"""limpa o terminal"""
import os
def main():
    '''metodo principal'''
    print('\n1 - Par ou Impar')
    print('2 - Classificação etária')
    print('3 - Login')
    print('4 - Quadrante das coordenadas')
    print('5 - Encerrar')
    opcao = int(input('Escolha uma operação: '))
    match opcao:
        case 1:
            os.system('cls')
            par_ou_impar()
        case 2:
            os.system('cls')
            classificar_idade()
        case 3:
            os.system('cls')
            validacao_senha()
        case 4:
            os.system('cls')
            coordenadas_quadrante()
        case 5:
            os.system('cls')
            print('Programa encerrado com sucesso!')

def par_ou_impar():
    """verifica se e par ou impar"""
    num = int(input('Digite o número: '))
    if num%2 == 0:
        print('O número é par!')
    else:
        print('O número é impar!')
    main()

def classificar_idade():
    """classifica a idade entre criança, adolescente e adulto"""
    idade = int(input('Digite a idade: '))
    if idade <= 12:
        print('Criança')
    elif 13 <= idade <= 18:
        print('Adolescente')
    else:
        print('Adulto')
    main()

NOME_DE_USUARIO = 'luiz'
SENHA_DO_USUARIO = 'senha1234'

def validacao_senha():
    """valida usuario e senha"""
    nome = input('Digite o nome de usuário: ')
    senha = input('Digite a senha: ')
    if nome == NOME_DE_USUARIO and senha == SENHA_DO_USUARIO:
        os.system('cls')
        print('Acesso aprovado!')
    else:
        print('Acesso negado.')
    main()

def coordenadas_quadrante():
    """diz em qual quadrante se encontra as coordenadas passadas"""
    eixo_x = int(input('Digite o valor do eixo X: '))
    eixo_y = int(input('Digite o valor do eixo Y: '))

    if eixo_x > 0 and eixo_y > 0:
        print('A coordenada está no primeiro quadrante')
    elif eixo_x < 0 < eixo_y:
        print('A coordenada está no segundo quadrante')
    elif eixo_x < 0 and eixo_y < 0:
        print('A coordenada está no terceiro quadrante')
    elif eixo_x > 0 > eixo_y:
        print('A coordenada está no quarto quadrante')
    else:
        print('A coordenada está no eixo ou no ponto de origem')
    main()

main()
