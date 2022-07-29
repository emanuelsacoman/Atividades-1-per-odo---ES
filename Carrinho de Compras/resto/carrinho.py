escolha=5
lista=[]

while escolha !="0":
  print("Menu")
  print("0 - Fim")
  print("1 - Cadastra Produtos")
  print("2 - Confere Lista de Produtos")
  print("3 - Confirma Produto")
  print("4 - Mostra Total")
  escolha=input("Escolha uma opção:")
  if escolha =="0":
    escolha=input("Tem certeza que quer sair? 0 - Sim , 5 - Não")
  if escolha =="1":
    print("Cadastrando produto...")
    produto=input("Escolha o nome do produto:")
    quantidade=input("Escolha a quantidade do produto:")
    lista.append(["",produto,quantidade,0])
  if escolha=="2":
    print("Exibindo produtos...")
    contador=0
    for produto in lista:

      print(contador,"#",produto[0]," ",produto[1],"-",produto[2])
      contador=contador+1
  if escolha=="3":
    print("Confirmando produto...")
    posicao=input("Digite a posição do produto:")
    posicao_int=int(posicao)
    preco=input("Digite o preco do "+lista[posicao_int][1] +":")
    lista[posicao_int][0]="OK"
    lista[posicao_int][3]=preco
  if escolha=="4":
    print("Mostrando Todos Produtos...")
    print("Produtos que não foram comprados...")
    contador=0
    for produto in lista:
      if produto[0]=="":
        print(contador,"#",produto[0]," ",produto[1],"-",produto[2], "R$", produto[3])
        contador=contador+1
    print("Produtos que foram comprados...")
    contador=0
    precototal=0
    for produto in lista:
      if produto[0]=="OK":
        print(contador,"#",produto[0]," ",produto[1],"-",produto[2], "R$", produto[3])
        contador=contador+1
        precototal=precototal+int(produto[2])*float(produto[3])
    print("Preco Total: R$",precototal)


print("Fim do programa!")