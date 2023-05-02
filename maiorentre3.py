n1 = int(input("Digite o numero 1 "))
n2 = int(input("Digite o numero 2 "))
n3 = int(input("Digite o numero 3 "))
if n1 > n2 and n1 > n3:
    print("O numero 1",n1, " foi o maior")
elif n2 > n3 and n2 > n1:
    print("O numero " ,n2," foi o maior")
elif n1 == n2 or n2 == n3 or n3 == n1 or n1==n2==n3:
    print("Numeros iguais não tem um maior")
else:
    print("O numero" ,n3, "foi o maior")

