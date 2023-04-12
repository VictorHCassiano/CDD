n1 = int(input("Digite um numero: "))

if n1 <= 0:
    print("Digite um numero maior que 0")
else:
    for x in range(1, n1 + 1, 1):
        print(x)
