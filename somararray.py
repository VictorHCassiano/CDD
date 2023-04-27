tamanhoArray = int(input("Digite um numero"))
A = []
B = []
Soma = []
for x in range(tamanhoArray):
    A.append(int(input("Digite algo para preencher o array A:")))
    B.append(int(input("Digite algo para preencher o array B:")))

for x in range(tamanhoArray):
    Soma.append(A[x] + B[x])

print(B)
print(A)
print(Soma)
