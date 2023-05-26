lista = []
n16 = input()
a = list(n16)
base = 16
n10 = 0

while n16 != '':
    n10 = 0
    for elemento in a:
        if elemento == 'A':
            elemento = '10'
        if elemento == 'B':
            elemento = '11'
        if elemento == 'C':
            elemento = '12'    
        if elemento == 'D':
            elemento = '13'
        if elemento == 'E':
            elemento = '14'
        if elemento == 'F':
            elemento = '15' 
        elemento = int(elemento)
        lista.append(elemento)
    lista.reverse()

    for i in range(len(lista)):
        print(len(lista))
        pos = lista.index(lista[i])
        print("posicao", pos)
        r = (base ** pos) * lista[i]
        print('r',r)
        n10 = n10 + r
        print(n10)
    print(f'BASE16={n16} BASE10={n10} ')
    
    n16 = input()
    