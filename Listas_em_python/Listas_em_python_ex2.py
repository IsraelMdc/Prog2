# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa
# lista a média de cada aluno. Ao final. imprima o número de alunos com média
# maior ou igual a 7.0.

listaMedia = []
listaMaior = []
contador = 1
while contador < 3:
    nota1 = int(input(f"Digite a primeira nota do aluno {contador}: "))
    nota2 = int(input(f"Digite a segunda nota do aluno {contador}: "))
    nota3 = int(input(f"Digite a terceira nota do aluno {contador}: "))
    nota4 = int(input(f"Digite a quarta nota do aluno {contador}: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    listaMedia.append(media)
    if media >= 7:
        listaMaior.append(media)
    contador = contador + 1
print(listaMedia)
print(f"O total de alunos com média maior que 7 é: {len(listaMaior)}")