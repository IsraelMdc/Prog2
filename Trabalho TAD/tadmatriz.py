#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
# 
#Copyright 2023 Israel Magalhães e Júlio César da Silva
#
#
#Função que cria a matriz, recebe a quantidade linhas e colunas como parâmetro e retorna uma matriz
def cria_mat(qlinhas, qcolunas):
    #Lista que será usada como linhas
    lst=[]
    #Matriz que será retornada
    tadmat=[]
    #For que irá criar o número de linhas de entrada
    for linha in range(qlinhas):
        #For para criar o número de colunas
        for coluna in range(qcolunas):
            #Todos os valores são 0
            lst.append(0)
        tadmat.append(lst)
        lst=[]
    #Retorna a matriz criada
    return tadmat

#Função que multiplica duas matrizes e retorna o resultado em forma de matriz    
def multi_mat(tadA, tadB):
    #Se o tamanho de colunas da primeira matriz for igual ao de linhas da segunda matriz, a multplicação ocorre
    if len(tadA[0]) == len(tadB):
        #Cria a matriz que será o resultado da multplicação
        tadmatx=cria_mat(len(tadA), len(tadB[0]))
        #For que percorre as matrizes e multiplica linhas por colunas
        for linha in range(len(tadA)):
            for coluna in range(len(tadB[linha])):
                for coluna2 in range(len(tadA[linha])):
                    tadmatx[linha][coluna]+=tadA[linha][coluna2]*tadB[coluna2][coluna]

        #Retorna a matriz com o resultado
        return tadmatx
    else:
        #Retorna nada se a condição não for atendida 
        return None

#Função que negativa a matriz, multiplicando cada elemento por -1        
def  neg_mat(tadA):
    for linha in range(len(tadA)):
        for coluna in range(len(tadA[linha])):
            tadA[linha][coluna]=tadA[linha][coluna]*-1
    
    #Retorna a matriz negativada
    return tadA   

#Função que soma duas matrizes
def soma_mat(tadA, tadB):
    #Se as matrizes possuirem o mesmo tamanho de linhas e colunas, a soma ocorrerá
    if (len(tadA) == len(tadB)) and len(tadA[0]) == len(tadB[0]):
        #Cria a matriz que será o resultado
        lst_out=cria_mat(len(tadA), len(tadA[0]))
        #Percorre linha por linha, coluna por coluna, somando-as
        for linha in range(len(tadA)):
            for coluna in range(len(tadA[linha])):
                lst_out[linha][coluna]=tadA[linha][coluna]+tadB[linha][coluna]
       #Retorna a matriz criada
        return lst_out
    else:
        #Retorna nada se a condição não for atendida 
        return None

#Função que tranposta a matriz   
def  transp_mat(tadA):
    #Cria a matriz tranposta
    tadTA=cria_mat(len(tadA[0]), len(tadA))
    #Altera os valores da matriz tranposta com os correspondentes 
    for linha in range(len(tadA)):
        for coluna in range(len(tadA[linha])):
            tadTA[coluna][linha]=tadA[linha][coluna]
    #Retorna a matriz criada
    return tadTA
    
#Função que recebe o nome de um arquivo, lê e cria uma matriz
def carrega_mat(nomearq):
    #Adiciona a extensão .txt
    nomearq+=".txt"
    #Abre o arquivo para leitura
    arquivo = open(nomearq , 'rt')
    lista = []
    #Lê a primeira linha do arquivo
    linha = arquivo.readline()
    
    #Enquanto a linha não for vazia, ele irá continuar a ler
    while linha != "":
        #Transforma a linha lida em uma lista
        linhatratada = linha.strip().split('    ')
        #Transforma os valores em inteiros
        for i in range(len(linhatratada)):
            linhatratada[i] = int(linhatratada[i])
        #Adiciona a linha lida na lsita
        lista.append(linhatratada)
        #Lê a próxima linha
        linha = arquivo.readline()
    #Fecha o arquivo
    arquivo.close()
    #Retorna a matriz
    return lista  

#Função que salva a matriz
def salvamat(tadmat,nomearq):
    #Abre o arquivo para escrita
    arq = open(nomearq,"wt")

    matriz_saida = ""
    #Percorre a matriz
    for i in range(len(tadmat)):
        for j in range(len(tadmat[i])):
            #Formata a saída
            matriz_saida += (f"{tadmat[i][j]:>6}")
        matriz_saida += '\n'
    #Escreve no arquivo    
    arq.write(f"{matriz_saida}")
    #Fecha o arquivo
    arq.close()
    #Retorna a matriz
    return tadmat