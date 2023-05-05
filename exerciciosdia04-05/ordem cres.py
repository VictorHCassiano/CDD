while True:
    n1 = int(input("Digite o numero 1: "))
    n2 = int(input("Digite o numero 2: "))
    while n1 == n2:
        n2 = int(input("Numeros nao podem ser iguais, Digite um diferente::"))
    if n1 < n2:
        print(n1, ",", n2)
    else:
        print(n2, ",", n1)
    confirmar = input("Deseja continuar? S/N: ")
    if confirmar == "N":
        break
