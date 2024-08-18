import random

def merge_sort(arr):
    """
    Ordena uma lista dada em ordem crescente usando o algoritmo de merge sort.
    Parâmetros:
    arr (list): A lista a ser ordenada.
    Retorna:
    list: A lista ordenada em ordem crescente.
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    """
    Une duas listas ordenadas em uma única lista ordenada.
    Parâmetros:
        left (list): A primeira lista ordenada.
        right (list): A segunda lista ordenada.
    Retorna:
        list: Uma nova lista contendo todos os elementos das duas listas de entrada, ordenados em ordem crescente.
    """
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    
    return merged

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

