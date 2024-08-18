def verifica_primos_na_lista(num):
    res = num%2
    if res == 0:
        return False
        
def maior_numero(list):
    maior = 0
    for num in list:
        if num > maior:
            maior = num
    return print(f"O maior número da lista {list} é: {maior}\n") 

def main():
    lista = [21,25,27,40,50,223,83,222]
    maior_numero(lista)
    for num in lista:
        if (verifica_primos_na_lista(num) == False):
            print(f"O número {num} não é primo")
        else:
            print(f"O número {num} é primo")
main()