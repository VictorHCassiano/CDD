nota1 = float(input("Digite a nota 1:"))

nota2 = float(input("Digite a nota 2:"))

nota3 = float(input("Digite a nota 3:"))
print(sum(nota1,nota2))

media = (nota1+nota2+nota3)/3

if media >= 7:
    print(f"Sua media é {media:.1f} aprovado")
elif media <= 4:
    print(f"Sua media é {media:.1f} voce esta de recuperacão")
else:
    print(f"Sua media é {media:.1f} reprovado")


