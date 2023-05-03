eleitores = int(input("Eleitores:"))
votosbrancos = int(input("Votos Brancos: "))
votosnulos = int(input("Votos Nulos: "))
votosvalidos = int(input("Votos Validos:"))

pervalidos = (votosvalidos/eleitores)*100
pernulos = (votosnulos/eleitores)*100
perbrancos = (votosbrancos/eleitores)*100

if eleitores != votosbrancos+votosnulos+votosvalidos:
    print("Eleicao fraudada")
else:
    print("Percentual:", "\nValidos:", pervalidos, "\nNulos:", pernulos, "\nBrancos", perbrancos)
