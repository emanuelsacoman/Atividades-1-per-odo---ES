def atividade2():
    n = int(input("Digite a quantidade de elementos do vetor: "))
    vetorA = [None] * n

    for x in range(n):
        vetorA[x] = int(input("Numero {}: ".format(x+1)))
    valor = int(input("Digite um novo valor: "))
    vetorA.append(valor)
    vetorA.insert(1,20)
    if n >= 9:
        del vetorA[7]
        print(vetorA)
    else:
        print(vetorA)
if __name__ == "__main__":
    atividade2()