import tadretangulo as td

def carregaLstLotes(nomearq):
    lst_lotes = []
    
    arqin = open(nomearq, "rt")
    linha = arqin.readline()
    while linha != "":
        lst = linha.strip().split(",")
        lote = td.cria(float(lst[1]), float(lst[2]),float(lst[3]),float(lst[4]))
        dicc = {"dono":lst[0],
                "lote":lote,
                "cont": 0
                }
        lst_lotes.append(dicc)
        linha = arqin.readline()
    arqin.close()

    return lst_lotes

def contabois(nomearq):
    lst = []
    arqin = open(nomearq, "rt")
    linha = arqin.readline()
    print("linha:",linha)
    while linha != "":
        print("passou")
        lst = linha.strip().split(", ")
        lote = td.cria(float(lst[1]), float(lst[2]))
        print(lote)
        dicc = {"dono":lst[0],
                "lote":lote,
                "cont": 0
                }
        lst.append(dicc)
        linha = arqin.readline()
    arqin.close()

    return lst
def main():
    lst_lotes = carregaLstLotes("TAD\\lotes.txt")
    print(lst_lotes) 
    lst_bois = contabois("TAD\\boisxy.txt")
    print(lst_bois)
main()