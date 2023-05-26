def salva_dic_cep(diccep,nomearq):
  arqout = open(nomearq,"wt")
  for k in diccep:
    arqout.write(k + ": " + str(diccep[k]) + "\n\n")
  arqout.close()
# fim salva_dic_cep

def monta_dic_cep(nomearq):
  arqin = open(nomearq,"rt")

  d = {}

  linha = arqin.readline().strip()

  while linha != "":
    lst = linha.split(",")
    cep = lst[2].strip()
    num = int(lst[1].split()[-1])

    if cep not in d:
      d[cep] = [num]
    else:
      d[cep].append(num)

    linha = arqin.readline().strip()
  # fim while

  arqin.close()

  return d
# fim monta_dic_cep

def main():
  diccep = monta_dic_cep("bdcepsruas.txt")
  salva_dic_cep(diccep,"dicsaida.txt")
  print("Processamento concluído!!")
# fim main

main()