def seis(a,d,t):

    dn=0 #contador para disciplina
    # d = n/ de disciplinas
    # a = n/ de alunos
    # t = n/ de turmas
    for i in range(t):
        for j in range (d):
            dn = dn+1
            notas=0
            k=0
            while k < a:
                nota = int(input("Digite a nota do aluno: "))
                notas = nota+notas 
                k=k+1
            media=notas/a
            print("A média da turma na disciplina {0} é: {1}".format(dn,media))            
if __name__ == "__main__":
    turmas = int(input("Informe o número de turmas: "))
    disciplinas = int(input("Informe o número de disciplinas: "))
    alunos = int(input("Informe o número de alunos: "))
    seis(alunos, disciplinas, turmas)