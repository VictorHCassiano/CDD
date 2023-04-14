numero = int(input("Digite um numero: "))
i = 0
for x in range(numero+2):
    for y in range(x):
        print(i, end=" ")
        i += 1
    i = 0
    print()
