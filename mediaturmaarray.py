notas = []
notasacimadamedia = 0
media = 0
for x in range(5):
    nota = int(input("Digite a nota: "))
    notas.append(nota)

for y in range(5):
    media += notas[y]

resultadomedia = media/5

for z in range(5):
    if notas[z] >= resultadomedia:
        notasacimadamedia += 1

print("A media foi", resultadomedia, "e tiveram", notasacimadamedia, "notas acima da media")
