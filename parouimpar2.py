n1 = int(input("Digite um numero: "))
while n1 == 0:
    n1 = int(input("Digite um numero: "))
if n1 % 2 == 0:
    if n1 > 0:
        print("Par, Positivo")

    elif n1 < 0:
        print("Par, Negativo")
elif n1 % 2 != 0:
    if n1 > 0:
        print("Impar, Positivo")
        
    elif n1 < 0:
        print("Impar, Negativo")


