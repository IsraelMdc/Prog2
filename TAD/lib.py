def criar(a,b,c):
    dicEquacao = {"ax**2":a,"bx":b,"c":c}
    return dicEquacao

def quantraizaes(dicEquacao):
    import numpy
    a = dicEquacao["ax**2"]
    b = dicEquacao["bx"]
    c = dicEquacao["c"]
    delta = b**2-4*a*c
    if numpy.sqrt(delta) > 0:
        return 2
    if numpy.sqrt(delta) == 0:
        return 1
    if numpy.sqrt(delta) < 0:
        return "Não existe solução dentro do conjunto de números reais"
    
    
def geta(a):
    return a

def getb(b):
    return b

def getc(c):
    return c
