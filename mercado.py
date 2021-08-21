from typing import List, Dict
from time import sleep

from models.produlto import Produlto
from utils.helper import formata_float_str_moeda


produltos: List[Produlto] = []
carrinho: List[Dict[Produlto, int]] = []


def main() -> None:
    menu()
    
def menu() -> None:
    print('===================================')
    print('=========== Bem-Vindo(a) ==========')
    print('=========== Python Shop ===========')
    print('===================================')
    
    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar produlto')
    print('2 - Listar produlto')
    print('3 - Comprar produlto')
    print('4 - Visualiar Carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair do Sistema')
    
    opcao: int = int(input())
    
    if opcao == 1:
        cadastrar_produlto()
    elif opcao == 2:
        listar_produltos()
    elif opcao == 3:
        comprar_produlto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção Inválida!')
        menu()
    
        
def cadastrar_produlto() -> None:
    print('Cadastro de Produlto')
    print('====================')
    
    nome: str = input('Informe o nome do produlto: ')
    preco: float = float(input('Informe o preço do produlto: '))
    
    produlto: Produlto = Produlto(nome, preco)
    
    produltos.append(produlto)
    
    print(f'O produlto {produlto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()
    

def listar_produltos() -> None:
    if len(produltos) > 0:
        print('Listagem de produltos')
        print('---------------------')
        for produlto in produltos:
            print(produlto)
            print('-----------------')
            sleep(1)
    else:
        print('Ainda não existem produltos cadastrados.')
    sleep(2)
    menu()

def comprar_produlto() -> None:
    if len(produltos) > 0:
        print('Informe o código do produlto que deseja adicionar ao carrinho: ')
        print('---------------------------------------------------------------')
        print('================== Produltos Disponíves =======================')
        for produlto in produltos:
            print(produlto)
            print('-----------------------------------------------------------')
            sleep(1)
        codigo: int = int(input())
        
        produlto: Produlto = pegar_produlto_por_codigo(codigo)
        
        if produlto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produlto)
                    if quant:
                        item[produlto] = quant + 1
                        print(f'O produlto {produlto.nome} agora possui {quant + 1} unidades do carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produlto: 1}
                    carrinho.append(prod)
                    print(f'O produlto {produlto.nome} foi adicionado ao carrinho.')
                    sleep(2)
                    menu()
                    
            else:
                item = {produlto: 1}
                carrinho.append(item)
                print(f'O produlto {produlto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()
        else:
            print(f'O produlto com código {codigo} não foi encontrado.')
            sleep(2)
            menu() 
    else:
        print('Ainda não existem produltos para vender.')
    sleep(2)
    menu()

def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produltos no carrinho: ')
        
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade {dados[1]}')
                print('----------------------')
                sleep(1)
        
    else:
        print('Ainda não existem produltos no carrinho.')
    sleep(2)
    menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0
        
        print('Produltos do carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('---------------------------------')
                sleep(1)
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')
        print('Volte sempre!')
        carrinho.clear
        sleep(5)
    else:
        print('Ainda não existem produltos no carrinho.')
    sleep(2)
    menu()
    
    
def pegar_produlto_por_codigo(codigo: int) -> Produlto:
    p: Produlto = None
    
    for produlto in produltos:
        if produlto.codigo == codigo:
            p = produlto
    return p


if __name__== '__main__':
    main()