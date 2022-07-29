def tres(a,b):
    i=0
    while a != b:
        for i in range (a+1,b):
            print("{}".format(i))
        a = int(input("Digite um número: "))
        b = int(input("Digite um número: ")) 

if __name__ == "__main__":
    a = int(input("Digite um número: "))
    #a=a+1
    b = int(input("Digite um número: "))
    tres(a,b)