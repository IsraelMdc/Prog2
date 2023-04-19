# Construa a função processa(<nome do arquivo>): <lista D>.
#  A função deve:
#  i) abrir o arquivo referenciado pelo 1o parâmetro, 
# ii) ler linha a linha (.readline()) testando o fim do arquivo para cada linha, 
# iii) fechar o arquivo ao final da função.
#  A função retorna como saída uma lista tipo D.
#  A organização de uma lista tipo D está expressa na figura 1.b.

def processa(arq):# <lista D>
    listaD = []
    listadominio = []
    i = 0
    arquivo = open(f'{arq}',"rt")
    linha = arquivo.readline()
    
    if linha[-1] == '\n':
        elemento = linha[:-1]
        listaD.append(elemento)

    for linha in arquivo:
        adicionou = True
        i=0
        if linha[-1] == '\n':#retira o /n
            elemento = linha[:-1]
            a = elemento[-2:]
            listadominio.append(a)
            # for i in range(len(listadominio)):
            #     if a == listadominio[i] not in listadominio:
            #         listadominio.append(a)  
            while i < len(listaD) and adicionou:
                # print("passou while")
                if a == listaD[i][-2:] or len(listaD) == i:
                    listaD.append(elemento) 
                    adicionou = False
                    i = 0
                    # print("passou if")
                i+=1             
    print(listaD)
    print(listadominio)
    arquivo.close()

    return listaD

def main():
    arq = "C:\\Users\\israe\\Desktop\\Federal\\Programação 2\\Prog2\\Prog2\\Tarefa Prova 1\\webdomains.txt"
    listaD = processa(arq)
if __name__ == '__main__':
    main()