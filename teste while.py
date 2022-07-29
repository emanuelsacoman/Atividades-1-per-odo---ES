def notas(n):
    soma = 0
    k = 0
    while(k < n):
        nota = float (input("Digite a nota: "))
        soma = soma+nota
        k = k + 1
    media = soma/n
    print("Média = {}".format(media))

if __name__ == "__main__":
    n = int(input("Digite o número de alunos: "))
    notas(n)
