def tabuada(n):
    for i in range(n+1):
        mult=i*n
        print("{0} X {1} = {2}".format(n,i,mult))


if __name__ == "__main__":
    n = int(input("Digite um número: "))
    tabuada(n)