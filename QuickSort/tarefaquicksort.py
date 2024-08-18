import json
import modquicksort

def carregabd(arqdir):
    lst = []
    lista = []
    arq = open(arqdir, "rt")

    for linha in arq:
        lst = linha.strip().replace(" ", "").split(",")

        elemento = json.dumps({"placa": lst[0],
                               "modelo": lst[1],
                               "marca": lst[2],
                               "km": lst[3],
                               "cor": lst[4],
                               "fuel": lst[5]})

        elemento = json.loads(elemento)
        
        lista.append(elemento)

    return lista

def main():
    lista = []
    qck = []    
    qcknr = []

    arqdir = "bdveiculos2.txt"

    lista = carregabd(arqdir)

    # Quick sort recursivo
    qck = modquicksort.quicksort(lista, "fuel")

    # Quick sort não recursivo
    qcknr = modquicksort.quicknr(lista, "fuel")

    with open("quickrout.txt", "w") as q:
        for line in qck:
            q.write(f"{line}\n")

    with open("quicknr-out.txt", "w") as qnr:
        for line in qcknr:
            qnr.write(f"{line}\n")

main()