Nalunos = int(input("Digite o numero de alunos: "))
contador = 0
soma = 0
while contador < Nalunos:
    notaAluno = int(input("Digite a nota do aluno: "))
    soma = soma + notaAluno
    contador += 1


media = soma/Nalunos
print("A média da turma é ", media)

