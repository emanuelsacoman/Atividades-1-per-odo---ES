def oito():
    i=0
    n=int(input("Digite o numero a ser fatorado: "))
    n_fat=1
    for i in range(2,n+1):
        n_fat=n_fat*i
    print("{}! = {}.".format(n,n_fat))
if __name__ == "__main__":
    oito()