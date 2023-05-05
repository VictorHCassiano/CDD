A = []
cont = 0
Nimpares = 0
while cont < 10:
    if Nimpares % 2 != 0:
        A.append(Nimpares)
        cont += 1
    Nimpares += 1
print(A)
