# 5. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine
# quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

cont = 0
idade = int
altura = int
mediaAltura = 0
contaMinions = 0
somaAltura = 0
listaIdade = []
listaAltura = []

while cont != 3:
    idade = int(input(f"Digite a idade do aluno {cont + 1}: "))
    altura = int(input(f"Digite a altura em centimetros do aluno {cont + 1}: "))
    listaAltura.append(altura)
    listaIdade.append(idade)

    cont = cont + 1

for altura in listaAltura:
    somaAltura += altura  
   
mediaAltura = somaAltura/len(listaAltura)
print(f"Média de alturas da turma: {mediaAltura}\n")

for i in range(len(listaIdade)):
    if listaIdade[i] > 13 and listaAltura[i] < mediaAltura:
        contaMinions = contaMinions + 1

print("Lista Idade = ",listaIdade)
print("Lista Altura em Centimetros = " ,listaAltura)
print("Alunos com mais de 13 anos abaixo da média de altura: ",contaMinions)