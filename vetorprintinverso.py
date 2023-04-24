numeros = []
for x in range(5):
    numero = int(input("Digite um numero: "))
    numeros.append(numero)

for y in range(4, -1, -1):
    print(numeros[y], end=' ')
