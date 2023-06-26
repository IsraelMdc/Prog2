from tadmatriz import *

def main():
   arqIn=open("Trabalho TAD\TAD - Matriz\matops.txt", "rt")
   linha= arqIn.readline()
   
   
   while linha!="":
        lst=linha.strip().split()
        print(lst)
                
        if "-" in lst[0]:
            nome=lst[0].split("-")
            print(nome)
            if len(nome)==2:
                print("passou 1")
                tadA=carrega_mat(nome[1] + ".txt")
                tadA=neg_mat(tadA)
            
        if "-" in lst[2]:
            nome=lst[2].split("-")
            if len(nome)==2:
                print("passou 2")
                tadB=carrega_mat(nome[1] + ".txt")
                tadB=neg_mat(tadB)
                   
        if "T" in lst[0]:
            nome=lst[0].split("T")
            print(nome)
            if len(nome)==2:
                print("passou 3")
                tadA=carrega_mat(nome[1] + ".txt")
                tadA=transp_mat(tadA)
        if "T" in lst[2]:
            nome=lst[2].split("T")
            print(nome)
            if len(nome)==2:
                print("passou 4")
                tadB=carrega_mat(nome[1] + ".txt")
                tadB=transp_mat(tadB)
            
        else:
            print("passou direto")
            tadA=carrega_mat(lst[0] + ".txt")
            tadB=carrega_mat(lst[2] + ".txt")
            
            if lst[1] == "x":
                tadC=multi_mat(tadA,tadB)
            if lst[1] == "+":
                tadC=soma_mat(tadA,tadB)
            
            tadC=salvamat(tadC, "teste.txt")
            
        linha= arqIn.readline()
    
main()