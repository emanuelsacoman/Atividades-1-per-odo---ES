#def show():
#    soma = 0
    
#    while soma < 7:
#        soma = soma + 1
#        print("{}".format(soma))
    

#if __name__ == "__main__":

#    show()

##########

#def inteiros(a,b):
#    soma = 0
#    while a%2 == 0 and b%2 == 0:
#        print(a+b)
#        print("Erro, digite novamente. ")
#        if a%2 == 0 and b%2 == 0:
#            soma = soma + a+b
        
#        a = int (input("Digite um número: "))
#        b = int (input("Digite outro número: "))
#    print("correto. ")
#    print("soma = {}".format(soma))
    
#if __name__ == "__main__":
#    a = int (input("Digite um número: "))
#    b = int (input("Digite outro número: "))
    
#    inteiros(a,b)

##########

#def tabuada(x):
#    k=1
#    while k <= 10:
#        print(x*k)
#        k=k+1
        
#if __name__ == "__main__":
#    numero=int(input("Digite um número: "))
    

#    tabuada(numero)

##########

#def idade():
#    m = 0
#    f = 0
#    soma2 = 0
#    i = 0
#    soma=0
#    while i <= 10:
#        idade = int (input("Quantos anos o usuário têm? "))
#        sexo = str (input("M - masculino | F - feminino "))
#        
#        if sexo == "M" or sexo == "m":
#            soma=idade+soma
#            m=m+1
#        elif sexo == "F" or sexo == "f":
#            soma2=idade+soma2
#            f=f+1
#        else:
#            print("erro")

#        i = i+1
    
#    media = soma/m
#    media2 = soma2/f
    
#    total = m+f
#    porm = m*100/total
#    porf = f*100/total
    
#    print("|")
#    print("| Média de idade dos usuários M: {0} | Média de idade dos usuários F: {1}".format(media, media2))
#    print("| Porcentagem de usuários M é : {0}% | E de F: {1}%".format(porm, porf))
#    print("|")
    
    

#if __name__ == "__main__":
    
#    idade()

##########

#def pares():
#    n = 1
#    soma = 0
#    s = 0
#    while n <= 15 and n > 0:
#        if n%2==0:
#            print("{}".format(n))
#            soma = n+soma
#            s=s+1
#        n = n+1
#    print("A soma dos valores é: {0} | E a quantidade total é: {1}".format(soma,s))    


#if __name__ == "__main__":
#    pares()

##########

#def tabuada():
#    tecla = '1'
#    while (tecla != '0'):
        
#        k = 0
#        tabuada = int(input("Digite um valor para calcular sua tabuada: "))
#        while k <= 10:
#            print(tabuada,'x',k,'=',tabuada*k)
#            k=k+1
#        tecla = input("Para calcular novamente, precione S | Para encerrar, precione 0 ")
#        while tecla != '0' and tecla != 'S' and tecla != 's' :
#            tecla = input("'S' para ir novamente e '0' para sair. ")
#    else:
#        print("Agradeço por usar o programa. ^^ ")
#if __name__ == "__main__":
    
#    tabuada()

##########

#def a():

#if __name__ == "__main__":

##########

def tabuada():
    tecla = '1'
    while (tecla != '0'):
        
        k = 0
        tabuada = int(input("Digite um valor para calcular sua tabuada: "))
        while k <= 10:
            print(tabuada,'x',k,'=',tabuada*k)
            k=k+1
        tecla = input("Para calcular novamente, precione S | Para encerrar, precione 0 ")
        while tecla != '0' and tecla != 'S' and tecla != 's' :
            tecla = input("'S' para ir novamente e '0' para sair. ")
    else:
        print("Agradeço por usar o programa. ^^ ")
if __name__ == "__main__":
    
    tabuada()

##########

def valores_inteiros():
    x = int(input("digite um numero "))
    y = int(input("digite um numero "))
    cont = x
    cont2 = y
    if x > y and y < x:
        while cont > y :
            cont = cont - 1 
            print(cont) 
            x = x - 1
    elif x < y and y > x:
        while cont2 > x :
            cont2 = cont2 - 1 
            print(cont2) 
            y = y - 1
            
if __name__ == "__main__":
    valores_inteiros()

##########

def soma():
    numero = 1
    resultado = 0
    numinfo = 0
    while numero != 0:
        numero = int(input("Digite seu numero desejado: "))
        resultado = numero+resultado
        numinfo = numinfo + 1
    numinfo = numinfo-1
    print("Resultado da soma : {0} | Quantidade de números informados : {1}".format(resultado, numinfo))
if __name__ == "__main__":
    soma()

##########

def solution():
    k=0
    ageFinal=100
    
    while k<10:
        age=int(input("Digite a idade do aluno: "))
        if age<ageFinal:
            ageFinal=age
            k=k+1
        else:
            k=k+1
    print("A menor idade é: ",ageFinal)
if __name__ == "__main__":
    solution()

    
    



    
