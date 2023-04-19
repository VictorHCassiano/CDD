digitardenovo = 5
while digitardenovo != 6:
    digitardenovo = 0
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite um numero: "))

    while True:
        print("  Selecione uma operacao")
        print("1. Soma")
        print("2. Subtracao")
        print("3. Multiplicacao")
        print("4. Divisao")
        print("5. Digitar denovo")
        print("6. Sair")

        escolha = int(input(""))
        match escolha:
            case 1:
                print(n1+n2)
            case 2:
                print(n1-n2)
            case 3:
                print(n1*n2)
            case 4:
                print(n1/n2)
            case 5:
                break
            case 6:
                digitardenovo = 6
                break

