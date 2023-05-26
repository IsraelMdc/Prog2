import random

def strmat(mat):
  linhas = len(mat)
  colunas = len(mat[0])
  s = ""
  for i in range(linhas):
    for j in range(colunas):
      s = s + "%4d" % mat[i][j]
    s = s + "\n"
  return s
# fim strmat

def criamat(quant_linhas,quant_colunas):
  mat = []
  for i in range(quant_linhas):
    linha_mat = []
    for j in range(quant_colunas):
      linha_mat.append(random.randint(1,3))
    mat.append(linha_mat)
  return mat
# fim criamat

def printmat(mat):
  linhas = len(mat)
  colunas = len(mat[0])
  
  for i in range(linhas):
    for j in range(colunas):
      print("%4d" % mat[i][j],end="")
    print()
# fim printtmat

def salvamat2(nomearq,st):
  arq = open(nomearq,"wt")
  arq.write(st)
  arq.close()

def salvamat(nomearq,mat):
  arq = open(nomearq,"wt")

  linhas = len(mat)
  colunas = len(mat[0])
  
  for i in range(linhas):
    for j in range(colunas):
      arq.write("%4d" % mat[i][j])
    arq.write("\n")

  arq.close()
# fim salvamat

def main():
  A = criamat(2,3)
  st = strmat(A)  
  print(st)
  salvamat2("matA5x10.txt",st)
# fim main

main()
