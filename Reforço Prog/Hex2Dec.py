def b162b10():
    #entrada de dados
    lista = []
    base = 16
    n10 = 0
    n16 = input()
    #processamento dos dados
    while n16 != '':
        str2list = list(n16)
        for elemento in str2list:
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
            pos = lista.index(lista[i])
            r = (base ** pos) * lista[i]
            n10 = n10 + r
        #saida de dados
        print(f'BASE16={n16} BASE10={n10}')
        n16 = input()

def main():
    b162b10()

if __name__ == "__main__":

  main()
