def lista_donos(nomearq):
    arq = open(f"{nomearq}", "rt")
    linha = arq.readline

    while linha != '':
        for linha in arq:
            lista = linha.strip().split(", ")
    lista_donos = lista

    return lista_donos

def main():
    import tadretangulo as tdret
    nomearq_lotes = "C:\\Users\\israe\\Desktop\\Federal\\Programação 2\\Prog2\\Prog2\\TAD\\lotes.txt"
    lst_donos = lista_donos(nomearq_lotes)
    print(lst_donos)


main()