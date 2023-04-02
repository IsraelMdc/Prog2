# Faça um Programa que leia duas listas com 10 elementos cada. Gere uma terceira
# lista de 20 elementos, cujos valores deverão ser compostos pelos elementos
# intercalados das duas outras listas.

lista1 = []
lista2 = []
listaIntercalada = []
cont1 = 0
cont2 = 0
qtdElementos = 10
elemento = int

while cont1 != qtdElementos:  
    elemento = int(input(f"Digite o elemento {cont1 + 1} da lista 1: "))
    lista1.append(elemento)
    cont1 = cont1 + 1


while cont2 != qtdElementos:  
    elemento = int(input(f"Digite o elemento {cont2 + 1}: da lista 2: "))
    lista2.append(elemento)
    cont2 = cont2 + 1

for i in range(len(lista1)):
    listaIntercalada.append(lista1[i])
    listaIntercalada.append(lista2[i])

print(lista1)
print(lista2)
print(listaIntercalada)