numeroAlunos = int(input("Digite o numero de alunos: "))
arrayAlunos = []
for x in range(numeroAlunos):
    nome = input("Digite o nome do aluno ")
    arrayAlunos.insert(x, nome)
    #ou arrayAlunos.append(nome)
for y in range(numeroAlunos):
    print(arrayAlunos[y], y)

print(arrayAlunos)

