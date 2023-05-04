n1 = int(input("Digite um numero para saber se ele e primo: "))
cont = 0
for x in range(1,n1+1):
    if n1%x ==0:
        cont+=1

if cont == 2:
    print("Numero Primo")
else: 
    print("Nao e numero primo")
