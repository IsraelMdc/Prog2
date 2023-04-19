arq = "C:\\Users\\israe\\Desktop\\Federal\\Programação 2\\Prog2\\Prog2\\Reforço Prog\\dadosEntrada.txt"

lista = []
lista1 = []

def f_Input_Arq(arq):
    arquivo = open(f'{arq}',"rt")

    for linha in arquivo:
        if linha[-1] == '\n':
            elemento = linha[:-1]       
        else:
            elemento = linha
        lista.append(elemento)
    arquivo.close()
    return lista

def f_Calcula_Media(lista):
    media = 0
    for i in range(len(lista)):
        numero = lista[i]
        numero = int(numero)
        lista1.append(numero)
        media = numero + media
    media = media / len(lista1)
    return media
def main():
    lista = f_Input_Arq(arq)
    media = f_Calcula_Media(lista)
    
    print(f'A quantidade de alunos na turma é: {len(lista)}')
    print(f'A média de idades é de : {media}')

if __name__ == '__main__':
    main()

