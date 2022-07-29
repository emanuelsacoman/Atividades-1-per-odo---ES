def quatro():
    k=0
    b=0
    for k in range (k,10):
        a= int(input("Digite um número: "))
        if a < 0:
            b=b+1

        k=k+1
    print("Número de vezes informados números negativos: {}".format(b))

if __name__ == "__main__":

    quatro()