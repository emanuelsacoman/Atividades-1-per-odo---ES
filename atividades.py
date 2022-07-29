#def aluno(a,b):
#    if a >= 7 and a <= 10 and b >= 75:
#        print("Aprovado!")
#    elif a < 4 and a >= 0 and b < 75 and b > 0:
#        print("Reprovado.")
#    elif a < 7 and a > 4 and b >= 75:
#        print("Precisa fazer exame.")
#    else:
#        print("erro")

#if __name__ == "__main__":
#    nota = float (input("Digite sua nota: "))
#    presenca = int (input("Digite frequencia de presença (0 a 100): "))
#    aluno(nota,presenca)

###########################

#def A():    
#    idade = int (input("Qual sua idade? "))
    
#    if idade >= 18 and idade < 100:
#        print("Acesso concedido.")
#    else:
#        print("Acesso negado.")

#def C():
#    idade = int (input("Qual sua idade? "))
#    catB = str (input("Você possui habilitação na categoria B por no mínimo um(1) ano? (S/N)"))

#    if idade >= 18 and idade < 100 and catB == 'S':
#        print("Acesso concedido.")
#    else:
#        print("Acesso negado.")

#def D():
#    idade = int (input("Qual sua idade? "))
#    catB = str (input("Você possui habilitação na categoria B por no mínimo dois(2) anos? (S/N) "))

#    if idade >= 21 and idade < 100 and catB == 'S':
#        print("Acesso concedido.")
#    else:
#        print("Acesso negado.")

#def E():
#    idade = int (input("Qual sua idade? "))
#    catC = str (input("Você possui habilitação na categoria C por no mínimo um(1) ano? (S/N) "))

#    if idade >= 21 and idade < 100 and catC == 'S':
#        print("Acesso concedido.")
#    else:
#        print("Acesso negado.")

#if __name__ == "__main__":
#    categoria = str (input("Qual categoria você deseja fazer? "))

#    if categoria == 'A' or categoria == 'a':
#        A()
#    elif categoria == 'B' or categoria == 'b':
#        A()
#    elif categoria == 'C' or categoria == 'c':
#        C()
#    elif categoria == 'D' or categoria == 'd':
#        D()
#    elif categoria == 'E' or categoria == 'e':
#        E()
#    else:
#        print("erro")

###########################

print("1- File Duplo\n2- Alcatra\n3- Picanha\n\n")
tipo = int(input("Digite o tipo: "))
quantidade = int(input("Digite a quantidade comprada: "))
resposta = int(input("A compra será realizada com cartao Tabajara? 1p/ SIM - 2p/ NAO: "))

if tipo == 1:
    nome = "File Duplo"
    if quantidade <= 5:
        preco = quantidade * 4.90
    else:
        preco = quantidade * 5.80
        
if tipo == 2:
    nome = "Alcatra"
    if quantidade <= 5:
        preco = quantidade * 5.90
    else:
        preco = quantidade * 6.80

if tipo == 3:
    nome = "Picanha"
    if quantidade <= 5:
        preco = quantidade * 6.90
    else:
        preco = quantidade * 7.80

if resposta == 1:
    r = "SIM"

    desconto = ((preco * 5) /100)
    total = preco - desconto
else:
    r = "NAO"
    total = preco
    
print("\n***************************CUPOM FISCAL**************************************")
print("* Carne.......................................................... %s " %nome)
print("* Quantidade..................................................... %d KG " %quantidade)
print("* Preço......................................................... %2.f R$ " %preco)
print("* Cartao Tabajara................................................ %s " %r)
print("* Total com desconto............................................ %2.f R$ " %total)
print("******************************************************************************")

















    
