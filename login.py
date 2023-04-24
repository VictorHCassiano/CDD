senhas = []
nomes = []


for x in range(5):
    Nome = input("Digite um nome: ")
    nomes.append(Nome)
    Senha = input("Digite sua senha: ")
    senhas.append(Senha)

print("Agora faremos o Login")
login = input("Digite seu nome: ")
password = input("Digite sua senha: ")

for z in range(5):
    if nomes[z] == login and senhas[z] == password:
        print("LOGIN EFETUADO COM SUCESSO")
        break

