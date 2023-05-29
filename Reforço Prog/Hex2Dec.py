def str2int(n):
    lista = []
    n16 = n.upper()
    str2list = list(n16)
    for letra in str2list:
        if letra == 'A':
            letra = 10
        if letra == 'B':
            letra = 11
        if letra == 'C':
            letra = 12    
        if letra == 'D':
            letra = 13
        if letra == 'E':
            letra = 14
        if letra == 'F':
            letra = 15 
        letra = int(letra)
        lista.append(letra)
    lista.reverse()
    return lista 

def b162b10(lista):
    base = 16 
    n10 = 0 
    lst = [] 
    for i in range(len(lista)):  
        r = 0
        pos = lista.index(lista[i])
        r = (base ** pos) * lista[i]
        lst.append(r)
    
    for n in lst:
        n10 = n + n10 
    
    return n10

def resultado(n16,n10):
    print(f'BASE16={n16} BASE10={n10}')

def main():
    n16 = input()

    while n16 != '':
        lst = str2int(n16)
        n10 = b162b10(lst)
        resultado(n16,n10)
        n16 = input()

if __name__ == "__main__":

  main()
