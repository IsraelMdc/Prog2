lista = []
base = 16
n10 = 0 
r = 0
lst = []
n16 = input()
while n16 != '':
    n10 = 0
    n16 = n16.upper()
    str2list = list(n16)
    lista = []
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
    
    for i in range(len(lista)):  
        pos = lista.index(lista[i])
        r = (base ** pos) * lista[i]
        lst.append(r)
        r = 0
        print(lst)
    #SOMA 
    n10 = 0 
    for n in lst:
        n10 = n + n10 
        print(n10)
    print(f'BASE16={n16} BASE10={n10}')
    n16 = input()