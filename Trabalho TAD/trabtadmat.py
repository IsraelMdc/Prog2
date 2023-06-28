# -*- coding: utf-8 -*-
#
# 
# 
#Copyright 2023 Israel Magalhães e Júlio César da Silva
#
#
#Importação do tadmatriz
import tadmatriz as tadm

#Declaração da função main
def main():

	#Abertura do arquivo que contém as operações, em modo leitura
	arquivo = open("matops.txt","rt")
	#Variável que irá ler linha por linha do arquivo
	arq = arquivo.readline()
	
	#Loop para percorrer todas as linhas
	while arq != "":
		# Fazer o split da linha obtida para uma lista
		linhaSplit = arq.split()

		# Definir variáveis para obter e salvar o resultado
		#Variável que recebe a letra da primeira matriz
		letraMatA = linhaSplit[0]
		#Variável para gerar o nome do arquivo final
		matriz1 = letraMatA
		#Variável que recebe o operador do cálculo
		operador = linhaSplit[1]
		#Variável que recebe a letra da segunda matriz
		letraMatB = linhaSplit[2]
		#Variável para gerar o nome do arquivo final
		matriz2 = letraMatB
		#Variável que irá receber o resultado dos cálculos
		resultado = []

		#Verifica se a primeira matriz precisa ser negativa e transposta
		if "T" in letraMatA and "-" in letraMatA:
			letraMatA = letraMatA[2]
			#Cria a matriz chamando a função, recebe como parãmetro uma string contendo o nome do arquivo
			matA = tadm.carrega_mat(letraMatA)
			#Transforma a matriz em seu transposta
			matA = tadm.transp_mat(matA)
			#Negativa a matriz
			matA = tadm.neg_mat(matA)
			#Adiciona os adjetivos da matriz na string que gera o nome do arquivo
			matriz1 = f"menostransp{letraMatA}"
			
		#Verifica se a segunda matriz precisa ser negativa e transposta
		elif "T" in letraMatB and "-" in letraMatB:
			letraMatB=letraMatB[2]
			#Cria a matriz chamando a função, recebe como parãmetro uma string contendo o nome do arquivo
			matB = tadm.carrega_mat(letraMatB)
			#Transforma a matriz em seu transposta
			matB = tadm.transp_mat(matB)
			#Negativa a matriz
			matB = tadm.neg_mat(matB)
			#Adiciona os adjetivos da matriz na string que gera o nome do arquivo
			matriz2 = f"menostransp{letraMatB}"
		else:
			#Verifica se a primeira matriz precisa ser negativa ou transposta
			if "T" in letraMatA or "-" in letraMatA:
				#Verifica se ela precisa ser tranposta
				if "T" in letraMatA:
					#Retira o T da string, para pode chamar a função que cria a matriz, lendo o arquivo que contém a matriz
					letraMatA = letraMatA[1]
					#Cria a matriz chamando a função, recebe como parãmetro uma string contendo o nome do arquivo
					matA = tadm.carrega_mat(letraMatA)
					#Tranposta a matriz a criada
					matA = tadm.transp_mat(matA)
					#Adiciona os adjetivos da matriz na string que gera o nome do arquivo
					matriz1 = f"transp{letraMatA}"
				#Verifica se ela precisa ser negativada
				if "-" in letraMatA:
					#Retira o - da string, para pode chamar a função que cria a matriz, lendo o arquivo que contém a matriz
					letraMatA=letraMatA[1]
					#Cria a matriz chamando a função, recebe como parãmetro uma string contendo o nome do arquivo
					matA = tadm.carrega_mat(letraMatA)
					#Negativa a matriz
					matA = tadm.neg_mat(matA)
					#Adiciona os adjetivos da matriz na string que gera o nome do arquivo
					matriz1 = f"menos{letraMatA}"
			#Se a primeira matriz não precisar de nenhum tratamento, ela é criada normalmente
			else:
				#Cria a matriz chamando a função, recebe como parãmetro uma string contendo o nome do arquivo
				matA = tadm.carrega_mat(letraMatA)
			
			#Verifica se a segunda matriz precisa ser negativa ou transposta
			if "T" in letraMatB or "-" in letraMatB:
				#Verifica se ela precisa ser tranposta
				if "T" in letraMatB:
					#Retira o T da string, para pode chamar a função que cria a matriz, lendo o arquivo que contém a matriz
					letraMatB=letraMatB[1]
					#Cria a matriz chamando a função, recebe como parãmetro uma string contendo o nome do
					matB = tadm.carrega_mat(letraMatB)
					#Tranposta a matriz a criada
					matB = tadm.transp_mat(matB)
					#Adiciona os adjetivos da matriz na string que gera o nome do arquivo
					matriz2 = f"transp{letraMatB}"
				
				#Verifica se ela precisa ser negativada
				if "-" in letraMatB:
					#Retira o - da string, para pode chamar a função que cria a matriz, lendo o arquivo que contém a matriz
					letraMatB=letraMatB[1]
					#Cria a matriz chamando a função, recebe como parãmetro uma string contendo o nome do arquivo
					matB = tadm.carrega_mat(letraMatB)
					#Negativa a matriz
					matB = tadm.neg_mat(matB)
					#Adiciona os adjetivos da matriz na string que gera o nome do arquivo
					matriz2 = f"menos{letraMatB}"
			
			#Se a primeira matriz não precisar de nenhum tratamento, ela é criada normalmente
			else:
				#Cria a matriz chamando a função, recebe como parãmetro uma string contendo o nome do arquivo
				matB = tadm.carrega_mat(letraMatB)

		# Obtenção dos resultados após realizar operações especificadas
		if operador=="+":
			#Chama a função que soma as matrizes
			resultado = tadm.soma_mat(matA, matB)
			#Adiciona a string para gerar o arquivo
			operador= "mais"
		if operador=="-":
			#Negativa a segunda matriz e a soma com a primeira 
			resultado = tadm.soma_mat(matA, tadm.neg_mat(matB))
			#Adiciona a string para gerar o arquivo
			operador= "menos"
		if operador=="x":
			#Multiplica as matrizes
			resultado = tadm.multi_mat(matA, matB)
			#Adiciona a string para gear o arquivo
			operador = "vezes"

		#if(resultado == None):
		#	print("Operação não conseguiu ser realizada.")

		#Define como será o nome do arquivo de saída com base nas operações realizadas
		outdir = f"{matriz1+operador+matriz2}.txt"
		#Chama a função que cria salvo a matriz criada
		tadm.salvamat(resultado,outdir)
		#Lê a proxima linha que contém as matrizes e operações que serão realizadas
		arq = arquivo.readline()
	
	#Fechamento do arquivo de leitura
	arquivo.close()
	
if __name__=="__main__":
	main()