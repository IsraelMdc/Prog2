def faxina(palavra):
	# Faxina no final da palavra
	while (palavra != "") and (not palavra[-1].isalnum()):
		palavra = palavra[:-1]	
		
	# Faxina no inicio da palavra
	if len(palavra) > 0:
		while not palavra[0].isalnum():
			palavra = palavra[1:]
		
	return palavra
# fim de faxina

def separa_pals(txt):
	lst = txt.split() # assume que o separador é o espaço, 1 caractere espaço.
	
	for i in range(len(lst)):
		if len(lst[i]) != 0:
			lst[i] = faxina(lst[i])
	
	return lst
# fim separa_pals

def print_tab_contagem(d):
	for palavra in d:
		print("%50s%8d" % (palavra ,d[palavra])) 
# fim print_tab_contagem

def main():
  doc = open("biblia-em-txt.txt","rt").read()
  lst_biblia = separa_pals(doc)
  
  diccont = {}

  for palavra in lst_biblia:
    if palavra.lower() not in diccont:
      diccont[palavra.lower()] = 1
    else:
      diccont[palavra.lower()] = diccont[palavra.lower()] + 1

	#print_tab_contagem(lst_palavras,lst_contagens)
	
  print("jesus apareceu",diccont["jesus"],"vezes.")
  print("diabo apareceu",diccont["diabo"],"vezes.")
	
  print("\nForam encontradas um total de",len(diccont),"palavras.")
# main

main()