while True:
    n1 = int(input("Digite um numero: "))
    while n1 == 0:
        n1 = int(input("NUMERO INVALIDO\nDigite outro numero: "))
    if n1 > 0:
        print("Positivo")
    elif n1 < 0:
        print("Negativo")
    confirmar = input("Deseja continuar S/N ")
    if confirmar == "N":
        break
