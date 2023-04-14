

contador = 0
senhacerta = "joao123456"

while contador < 3:
 senha = input("Digite sua senha: ")
 if senha == senhacerta:
    print("Bem vindo")
    break
 else:
    contador += 1
if contador == 3:
    print("SENHA BLOQUEADA")





