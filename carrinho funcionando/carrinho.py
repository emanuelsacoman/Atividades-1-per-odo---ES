import time     # Básicamente um "delay" da linguagem C.
def selecionar(dinheiro):
    escolha = 6
    carrinho = 0
    while escolha !="7":
        time.sleep(2)

        print(" //---""Saldo na Carteira : R$",dinheiro,"---\\")        
        print(" \---ITENS---/")          # Lista de itens.
        print("0 - pao R$5,0")                                                                                         
        print("1 - farinha R$35,0 ")                                           
        print("2 - leite R$40,0")                                    
        print("3 - nata R$10,0")                                             
        print("4 - manteiga R$80,0") 
        print(" \-------------/") 
        print(" \---OPÇÕES---/")        # Opções do carrinho.                                   
        print("5 - finalizar compra")  
        print("6 - Visualizar itens no carrinho")
        itens = ["pao","farinha","leite","nata","manteiga"]

        preco = [5.0,35.0,40.0,10.0,80.0]       #Armazena valores dos produtos.
        escolha=input("Escolha uma opção:")     # Opções para interação.
        if escolha== "0":#pao
            carrinho = carrinho + preco[0]
            carrinhoI.append(itens[0])
            print("Valor total: R$",carrinho)
            time.sleep(1)
        elif escolha== "1":#farinha
            carrinho = carrinho + preco[1]
            carrinhoI.append(itens[1])
            print("Valor total: R$",carrinho)
            time.sleep(1)
        elif escolha== "2":#leite
            carrinho = carrinho + preco[2]
            carrinhoI.append(itens[2])
            print("Valor total: R$",carrinho)
            time.sleep(1)
        elif escolha== "3":#nata
            carrinho = carrinho + preco[3]
            carrinhoI.append(itens[3])
            print("Valor total: R$",carrinho)
            time.sleep(1)
        elif escolha== "4":#manteiga
            carrinho = carrinho + preco[4]
            carrinhoI.append(itens[4])
            print("Valor total: R$",carrinho)
            time.sleep(1)
        elif escolha== "5":#finalizar compra
            if dinheiro >= carrinho:
                compraF = dinheiro - carrinho
                print("Compra efetuada com sucesso :) ")
                print("Saldo restante: R$",compraF)
                time.sleep(4)
                exit()

            else:
###############################


        elif escolha== "6":#visualizar itens do carrinho.
            print("Exibindo produtos...")
            print(carrinhoI)
            time.sleep(2)
        else:#caso o usuário insira alguma informação inválida.
            print("\---ERRO---/")
            time.sleep(1)

def carteira():     # Entrar com o valor inicial.                            
    d = float(input("Quantos reais você deseja adicionar a sua carteira?: "))
    print("seu saldo: R$",d)
    return d

if __name__ == "__main__":
    escolha = 2
    carrinhoI=[]    # Armazena itens que o usuário escolheu. [vetor]
    d =  carteira()
    
    while escolha !=0 :
        print("Menu")
        print("0 - Selecione produtos")                            
        print("1 - finalizar o programa ")
        escolha=input("Escolha uma opção: ")
        if escolha == "0":
            print("Selecionando produto... ")
            selecionar(d)
        elif escolha == "1":#termina o código.
            exit()
        else:#caso o usuário insira alguma informação inválida.
            print("\---ERRO---/")