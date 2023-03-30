time1 = input("Digite o nome do time 1: ")
time2 = input("Digite o nome do time 2: ")
goltime1 = int(input("Num de gol do time 1:"))
goltime2 = int(input("Num de gol time 2:"))

if goltime1 != goltime2:
    if goltime1 > goltime2:
        print(time1, "VENCEDOR")
    else:
        print(time2, "VENCEDOR")
else:
    print("EMPATE")
