produtos = {}

def adcionar():
        while True :
            nome = input('Digite o nome do produto : ')
            quantidade = int(input('Digite a quantidade do produto : '))
            valor = float(input('Digite o valor do produto : '))
            produtos [nome] = {
                'quantidade' : quantidade,
                'valor': valor
            }
            continuar = input('Desja continuar ? s/n ')
            if continuar != 's':
                break
        return produtos

def valores():
        valorGasto = 0 
        for produto in produtos.values():
            valorGasto += produto['quantidade'] * produto['valor']
        return valorGasto


def atulizar():
      while True:
            
            

def remover():
    removerPrduto = input('Deseja remover algum produto ? ')
    if removerPrduto == 's':
          selecionarProduto = input('Digite o produto que deseja remover : ')
          if selecionarProduto in produtos:
                del produtos[selecionarProduto]
                return f'o produto {selecionarProduto} foi removido com sucesso'
          else:
                return 'produto nao encontrado'




if __name__ == '__main__':
        adcionar()
        remover()
        print(produtos)
        print(f'Valor total gasto: R$ {valores():.2f}')
