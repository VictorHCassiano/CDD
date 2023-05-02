while True:
    base = int(input("Digite a base: "))
    altura = int(input("Digite a altura: "))
    area = (base*altura)/2
    print("A area do triangulo é:", area)

    confirmar = input("Deseja continuar? S/N: ")
    if confirmar == "N":
        break
