confirmacao = "S"
while confirmacao == "S":

    nota1va = float(input("NOTA 1-VA:"))

    while nota1va > 10 or nota1va < 1:
     nota1va = float(input("Digite uma nota de 1-10: "))
     if nota1va < 10 and nota1va > 1:
         break

    nota2va = float(input("NOTA 2-VA:"))
    while nota2va > 10  or nota2va < 1:
     nota2va = float(input("Digite uma nota de 1-10: "))
     if nota2va < 10 and nota2va > 1:
       break

    media = (nota1va+nota2va)/2
    print("A media foi ", (media) )
    confirmacao = input("Deseja continuar?\nS/N:")


    if confirmacao == "S" or "s":
       print()
    elif confirmacao == "N" or "n":
        print("Encerrando...")



