import merge_lib
import time

def main():
    # Criar uma lista de números para ordenar
    numbers = (merge_lib.create_random_list(10000))
    print("lista Original: ", numbers)

    # Começar a medir o tempo de execução do merge sort
    start_time = time.time()

    # Ordenar a lista usando o merge sort
    sorted_numbers = merge_lib.merge_sort(numbers)

    #Parar de medir o tempo de execução
    end_time = time.time()

    # Imprime o tempo de execução subtraidno o tempo final do tempo inicial
    print("Tempo de execução: ", end_time - start_time, "segundos")
    
    # Imprime a lista ordenada
    print("Lista ordenada: ", sorted_numbers)

if __name__ == "__main__":
    main()