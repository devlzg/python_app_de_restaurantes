"""Módulo que importa a função de limpar o terminal"""
import os
# pylint: disable=C0116
                # estrutura de dados chamada de dicionário
restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}]

def exibir_nome():
    """exibe o nome do programa"""
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
''')


def exibir_opcoes():
    """exibe as opcoes"""
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar/Desativar Restaurante')
    print('4. Sair\n')


def voltar_ao_menu_principal():
    """volta ao menu principal"""
    input('\nAperte Enter para retornar ao menu principal...')
    main()


def exibir_subtitulo(texto):
    """Exibe o subtitulo da funcionalidade sendo operada"""
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)

def opcao_invalida():
    """Retorna ao menu principal apos uma opcao invalida ser escolhida"""
    os.system('cls')
    print('Opção inválida!')
    voltar_ao_menu_principal()


def cadastrar_novo_restaurante():
    """
    Cadastra novos restaurantes e os armazena no dicionário
    
    Inputs:
    - nome do restaurante
    - categoria do restaurante
    
    Output:
    - adiciona um novo restaurante ao dicionario
    """
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input(
        'Digite o nome do restaurante que será cadastrado: ')
    categoria_do_restaurante = input(
        f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante,
                            'categoria': categoria_do_restaurante,
                            'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()


def listar_restaurantes():
    """Lista todos os dados de todos os restaurantes cadastrados"""
    exibir_subtitulo("Lista de restaurantes")
    print(f"\n{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Estado")
    for restaurante in restaurantes:
        # pega o nome do restaurante de dentro do dicionario
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    """Ativa ou desativa um restaurante específico"""
    exibir_subtitulo('Ativar/Desativar restaurante')
    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante[
                'ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
    voltar_ao_menu_principal()


def escolher_opcao():
    """funcao que processa a opcao escolhida"""
    # input automaticamente tem o tipo de string, então a função int realiza o "casting",
    # transformando o valor em inteiro
    try:
        opcao_escolhida = int(input('Digite o numero da opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:  # pylint: disable=W0702
        opcao_invalida()


def finalizar_app():
    """funcao que finaliza o app"""
    exibir_subtitulo("Programa encerrado.")


def main():
    """funcao principal"""
    os.system('cls')
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
