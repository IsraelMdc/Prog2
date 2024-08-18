import random

def create_random_list(N):
    """
    Gera uma lista de números inteiros aleatórios.
    Parâmetros:
    N (int): O número de números inteiros aleatórios a serem gerados.
    Retorna:
    list: Uma lista de números inteiros aleatórios.
    """
    
    random_list = []
    for _ in range(N):
        random_list.append(random.randint(1, 100))
    return random_list

def insert_sort(arr):
    """
    Ordena uma lista de elementos em ordem crescente usando o algoritmo de Ordenação por Inserção.
    Parâmetros:
    arr (list): A lista de elementos a ser ordenada.
    Retorna:
    list: A lista ordenada em ordem crescente.
    """
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
