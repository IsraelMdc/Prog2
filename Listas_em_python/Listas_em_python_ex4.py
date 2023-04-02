# Altere o programa anterior, intercalando 3 listas de 10 elementos cada

lista1 = []
lista2 = []
lista3 = []
listaIntercalada = []
cont1 = 0
cont2 = 0
cont3 = 0
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

while cont3 != qtdElementos:  
    elemento = int(input(f"Digite o elemento {cont3 + 1}: da lista 3: "))
    lista3.append(elemento)
    cont3 = cont3 + 1


for i in range(len(lista1)):
    listaIntercalada.append(lista1[i])
    listaIntercalada.append(lista2[i])
    listaIntercalada.append(lista3[i])

print(lista1)
print(lista2)
print(listaIntercalada)