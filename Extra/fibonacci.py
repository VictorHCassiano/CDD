n = int(input("Digite um número: "))
fib1 = 0
fib2 = 1
for i in range(1, n+1):
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib
    print(fib)
    
   