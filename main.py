produtos = {}

def adcionar():
        while True :
            nome = input('Digite o nome do produto : ')
            quantidade = int(input('Digite a quantidade do pr1duto : '))
            valor = float(input('Digite o valor do produto : '))
            produtos [nome] = {
                'quantidade' : quantidade,
                'valor': valor
            }
            continuar = input('Desja continuar ? s/n ').lower()
            if continuar != 's':
                break
        return produtos

def valores():
        valorGasto = 0 
        for produto in produtos.values():
            valorGasto += produto['quantidade'] * produto['valor']
        return valorGasto


def atualizar():
      while True:
            atualizarProduto = input('Digite atualizar algum produto ? ').lower()
            if atualizarProduto != 's':
                  break
            nome= input('Digite o nome do produto que deseja atualizar : ')
            if nome in produtos:
                  novaquantidade = int(input('Digite a quantidade de produtos : '))
                  novoValor = float(input('Digite o novo valor do produto : '))
                  produtos[nome]['quantidade '] = novaquantidade
                  produtos[nome]['valor']=novoValor
                  return f'o produto {nome} foi atualizado com sucesso '
            else:
                return 'produto não encontrado'            
            

def remover():
    removerPrduto = input('Deseja remover algum produto ? ').lower()
    if removerPrduto == 's':
          selecionarProduto = input('Digite o produto que deseja remover : ')
          if selecionarProduto in produtos:
                del produtos[selecionarProduto]
                return f'o produto {selecionarProduto} foi removido com sucesso'
          else:
                return 'produto nao encontrado'
        

if __name__ == '__main__':
        adcionar()
        atualizar()
        remover()
        print(produtos)
        print(f'Valor total gasto: R$ {valores():.2f}')
