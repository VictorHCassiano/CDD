A=[]
M=[]
for x in range(10):
    numero = int(input("Digite um numero: "))
    A.append(numero)

multiplicar = int(input("Digite um numero para multiplicar o vetor"))
for y in range(10):
  M.append(A[y]*multiplicar)

print(A, "\n", multiplicar, "\n", M)





