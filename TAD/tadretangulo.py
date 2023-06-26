# Retorna uma estrutura de dados que representa o TAD.
def cria_lh(xes,yes,l,a):
  return [xes,yes,l,a]

# Retorna uma estrutura de dados que representa o TAD.
def cria (xes,yes,xdi,ydi): 
  l = abs(xes-xdi)
  a = abs(yes-ydi)
  return [xes,yes,l,a]

def getES(tadret):
  return (tadret[0],tadret[1])

def getDI(tadret):
  return (tadret[0] + tadret[2],tadret[1] + tadret[3])

def getDS(tadret):
  xdi = getDI(tadret)[0]
  return (xdi,tadret[1])

def getEI(tadret):
  ydi = getDI(tadret)[1]
  return (tadret[0],ydi)

def getL(tadret):
  return tadret[2]

def getA(tadret):
  return tadret[3]

# Retorna o valor da área do retângulo.
def area(tadret):
  return tadret[2] * tadret[3]

# Retorna o valor do perímetro do retângulo.
def perimetro(tadret):
  return 2*tadret[2] + 2*tadret[3]
  
# Retorna True se x, y está no interior (ou borda) do retângulo, False caso 
def pertence(tadret,x,y):
  result = (abs(tadret[0] - x) <= tadret[2]) and (abs(tadret[1] - y) <= tadret[3])
  return result

def main():
  rA = cria_lh(10,10,30,15)
  px = 15
  py = 26
  print("Area:",area(rA))
  print("Perimetro:",perimetro(rA))
  print(pertence(rA,px,py))
  
if __name__ == "__main__":
  main()