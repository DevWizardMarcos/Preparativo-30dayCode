from main import * 

def menu():
    while True:
        print('HEHEHHEHEHE \n Projeto \n HEHEHEHHE')
        print('1 - Adicionar produtos')
        print('2 - Atualizar produtos')
        print('3 - Remover produtos')
        print('4 - Listar produtos')
        print('5 - mostrar produtos')
        print('0- Sair')
        opcao = input('Digite uma opção : ')

        if opcao == '1':
            adcionar()

        elif opcao == '2':
            atualizar()

        elif opcao == '3':
            remover()

        elif opcao == '4':
            print(produtos)

        elif opcao == '5':
            print(f'Valor total gasto: R$ {valores():.2f}')

        elif opcao == '0':
            print('encerrando....')
            break
        
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == '__main__':
    menu()