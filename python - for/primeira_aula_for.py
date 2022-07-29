def media(n):
    soma = 0
    for i in range(n):
        nota = float(input("Digite a nota: "))
        soma = soma+nota
    media = soma/n
    return media

if __name__ == "__main__":
    n=int(input("Digite o numero de alunos: "))
    m = media(n)
    print("Media da turma = {0:.2f}".format(m))