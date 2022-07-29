from lista_produtos import produtos                                               # Importa vetor "produtos" da pagina de listas.   
cesta = []


def fim():
    print("Fim do programa. ")

def selecionar(d):


def lista():
    print("Exibindo produtos...")
    contador = 0
    for produto in produtos:
        print(contador,"#",produto[0]," ",produto[1],"-",produto[2])
        contador=contador+1

def finalizar():
    print("Exibindo produtos na sua cesta...")
    contador = 0
        for ... in ...:

            contador=contador+1
    

def retirar():
    print("Quais itens gostaria de tirar da sua cesta? ")

def carteira(d):
    print("Você possui: R${} ".format(d))                                         # Deve atualizar conforme a compra

if __name__ == "__main__":
    dinheiro = float(input("Quantos reais você possuí em sua carteira? "))
    escolha = 6
    while escolha == 6:
        print("Menu")
        print("0 - Fim")                                                          # Encerra o programa;                                 //
        print("1 - Selecione produtos")                                           # Adiciona produtos à cesta;
        print("2 - Confere Lista de Produtos")                                    # Mostra a lista de produtos, quantidade e valor;
        print("3 - Finalizar Compra")                                             # Termina o programa e desconta da carteira;
        print("4 - Retirar Produto da Cesta")                                     # Tira o produto e volta o calor à carteira;
        print("5 - Ver carteira")                                                 # Visualiza sua carteira.                             //

    escolha=input("Escolha uma opção: ")
    
    if escolha == 0:
        a= int(input("Tem certeza? 0 - Fim | 6 - Retorna ao menu"))
        if a != 0:
            escolha = 6
        else:
            fim()
    elif escolha == 1:
        print("Selecionando produto... ")
        selecionar(dinheiro)
    elif escolha == 2:
        lista()
    elif escolha == 3:
        finalizar()
    elif escolha == 4:
        retirar()
    elif escolha == 5:
        carteira(dinheiro)
    else:
        print("erro")