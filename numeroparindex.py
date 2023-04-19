string = input("Digite alguma coisa")
numerostring = len(string)
for x in range(numerostring):

    if x % 2 == 0:
        print(string[x])