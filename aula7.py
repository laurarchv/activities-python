nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
nota4 = float(input('Quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 2
print(f"a média do aluno é = {media}")

if (media >= 63):
    print ("APORVADO")

else:
    print ("REPROVADO")