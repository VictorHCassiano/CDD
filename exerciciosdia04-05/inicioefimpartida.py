inicio = int(input("Digite quando o jogo comecou: "))
fim = int(input("Digite quando o jogo terminou: "))


if fim < inicio:
    print(fim+24-inicio)
else:
    print(fim-inicio)
