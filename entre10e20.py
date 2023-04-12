entre10e20 = 0
forade10e20 = 0
for x in range(10):
    n1 = int(input("Digite um numero: "))

    if n1 >= 10 and n1 <= 20:
        entre10e20 += 1
    elif n1 < 10 or n1 > 20:
        forade10e20 += 1


print("Foram", entre10e20, "no intervalo", "e", forade10e20, "fora do intervalo")
