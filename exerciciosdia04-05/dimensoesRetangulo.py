while True:
    escolha = int(input("Digite\n 1- Para triangulo\n2- Para retangulo\n3-Para sair\n"))

    match escolha:
        case 1:
            baseTriangulo = int(input("Digite a base do Triangulo: "))
            alturaTriangulo = int(input("Digite a altura do Triangulo: "))
            print((baseTriangulo * alturaTriangulo) / 2)
        case 2:
            alturaRetangulo = int(input("Digite a altura do retangulo: "))
            baseRetangulo = int(input("Digite a base do retangulo: "))
            print(alturaRetangulo * baseRetangulo)
        case 3:
            break

        case _:
            print("Opcao invalida")
    # if escolha == 1:
    #     baseTriangulo = int(input("Digite a base do Triangulo: "))
    #     alturaTriangulo = int(input("Digite a altura do Triangulo: "))
    #     print((baseTriangulo*alturaTriangulo)/2)
    # elif escolha == 2:
    #         alturaRetangulo = int(input("Digite a altura do retangulo: "))
    #         baseRetangulo = int(input("Digite a base do retangulo: "))
    #         print(alturaRetangulo*baseRetangulo)
    # elif escolha == 3:
    #     break
    # else:
    #     print("Opcao invalida")
