def atividade1():
    vetorA=[0,0,0,0,0]
    vetorB=[0,0,0,0,0]
    vetorC=[0,0,0,0,0]   

    for x in range(5):
        vetorA[x] = int(input("Numero {}: ".format(x+1)))
    for x in range(5):
        vetorB[x] = int(input("Numero {}: ".format(x+1)))
    
    vetorC = vetorA
    vetorA = vetorB
    vetorB = vetorC

    print("Vetor A: {0}, Vetor B: {1}".format(vetorA,vetorB))

if __name__ == "__main__":
    atividade1()