senhas = []
nomes = []


for x in range(5):
    Nome = input("Digite seu nome: ")
    nomes.append(Nome)
    Senha = input("Digite sua senha: ")
    senhas.append(Senha)

for y in range(5):
    print(nomes[y], senhas[y], y)
