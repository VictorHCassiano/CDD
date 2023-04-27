medias = []
while True:
    N1 = int(input("Digite a primeira nota:"))
    N2 = int(input("Digite a segunda nota:"))
    media = (N1+N2)/2
    medias.append(media)
    if media >= 7:
        print("Parabens Aprovado!!!")
    elif media >= 4 and media < 7:
        print("Recuperacao")
    else:
        print("Reprovado")

    confirmar =input("Quer colocar nota de outro aluno?\nS/N ")
    if confirmar == "N":
        print(medias)
        break
