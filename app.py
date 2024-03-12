import os
restaurantes = [{'Nome':'Shinpo', 'Categoria':'Comida Japonesa', 'Status': False}]

def exibir_logo():
    '''Essa funcao exibi a logo'''
    print('''
    █ █ █ █ █▄ █ █▀▀ █▀█ █▄█   █▀▀ █ █   █
    █▀█ █▄█ █ ▀█ █▄█ █▀▄  █    █▀  █ █▄▄ █▄▄
        ''')
    
def exibir_menu():
    '''Essa funcao exibe o menu'''
    print('1- Cadastrar restaurante')
    print('2- Listar restaurante')
    print('3- Altere o status')
    print('4- Sair\n')

def opcao_invalida():
    '''Essa funcao invalida qualquer resposta errada'''
    os.system('cls')
    print('Opção invalida\n')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    '''Essa funcao volta ao menu principal'''
    input('\nDigite uma tecla para retornar ao menu principal ')
    main()

def cadastro_de_restaurantes():
    '''Essa funcao cadastra os restaurantes'''
    os.system('cls')
    print('Castre um novo restaurante\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_restaurante = {'Nome': nome_do_restaurante, 'Categoria': categoria_restaurante, 'Status': False}
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso \n')
    restaurantes.append(dados_restaurante)
    voltar_ao_menu_principal()

def lista_restaurante():
    '''Essa funcao lista todos os restaurantes'''
    os.system('cls')
    print('Lista dos restaurantes cadastrados\n')
    for restaurante in restaurantes:
        nome = restaurante['Nome']
        categoria = restaurante['Categoria']
        status = 'Ativado' if restaurante['Status'] else 'Desativado'
        print(f'Nome: {nome} \n Categoria: {categoria} \n Status: {status}\n')
    voltar_ao_menu_principal()

def alterar_status_restaurante():
    '''Essa funcao altera o status dos restaurantes'''
    os.system('cls')
    print('Alterar o status do restaurante \n')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['Nome']:
            restaurante_encontrado = True
            restaurante ['Status'] = not restaurante ['Status']
            mensagem_ativado = f'O restaurante {nome_restaurante} foi ativado com sucesso'
            mensagem_desativado = f'O restaurante {nome_restaurante} foi desativado com sucesso'
    if restaurante['Status']:
            print(mensagem_ativado) 
    else:
        print(mensagem_desativado)   
    voltar_ao_menu_principal()

def escolha_opcao():
    '''Essa funcao serve para escolher a funcao no menu'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        match opcao_escolhida:
            case 1: cadastro_de_restaurantes()
            case 2: lista_restaurante()
            case 3: alterar_status_restaurante()
            case 4: finalizando_app() 
            case _: opcao_invalida()
    except:
        os.system('cls')
        opcao_invalida()

def finalizando_app():
    '''Essa funcao finaliza o app'''
    os.system('cls')
    print('Encerrando o aplicativo\n')

def main():
    '''Essa funcao cria um padrao de execucao para quando volta ao menu'''
    os.system('cls')
    exibir_logo()
    exibir_menu()
    escolha_opcao()

if __name__ == '__main__':
    main()
