import random
import time

def main():
    lst = [7, 2, 10, 5, 9, 12]

    for i in range(len(lst)-1):
        indice_menor_todos = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[indice_menor_todos]:
                indice_menor_todos = j 

        aux = lst[i]   
        lst[i] = lst[indice_menor_todos]
        lst[indice_menor_todos] = aux
    print(lst) 
main()