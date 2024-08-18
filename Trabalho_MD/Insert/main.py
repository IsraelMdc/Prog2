import insert_lib
import time

def main():
    # Create a list of numbers to sort
    numbers = (insert_lib.create_random_list(10000))
    print("lista Original: ", numbers)

    # Measure the execution time of merge sort
    start_time = time.time()
    # Sort the list using merge sort
    sorted_numbers = insert_lib.insert_sort(numbers)
    end_time = time.time()

    # Print the execution time
    print("Tempo de execução: ", end_time - start_time, "segundos")
    
    # Print the sorted list
    print("Lista ordenada: ", sorted_numbers)

if __name__ == "__main__":
    main()
    

