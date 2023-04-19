'''O arquivo webdomains.txt possui a organização mostrada na figura 1.a. Os valores e a
quantidade de dados são apenas exemplos, o arquivo real pode conter milhares de linhas.
Construa um programa Python chamado prova1.py. O programa processa o arquivo
webdomains.txt conforme o que é pedido a seguir:
a) Construa a função processa(<nome do arquivo>): <lista D>. A função deve: 
i)abrir o arquivo referenciado pelo 1o parâmetro, 
 ii) ler linha a linha (.readline())
testando o fim do arquivo para cada linha, 
iii) fechar o arquivo ao final da função. A
função retorna como saída uma lista tipo D. A organização de uma lista tipo D está
expressa na figura 1.b.

c) Construa a função main() para executar o seguinte processamento: Main deve
chamar a função do item (a) para processar o arquivo webdomains.txt e retornar
uma lista D. Em seguida, main de chamar a função do item (b) para criar um
arquivo chamado saidaprova1.txt a partir da lista D retornada pela chamada à
função processa(..).'''

def processa(nomearq):

  lst_d=[]
  
  lst_site=[]
  
  lst_domain=[]
  

  
  
  arq = open(f'{nomearq}.txt', 'rt')
  linha = arq.readline()

  while linha!= "":

    lst_site.append(linha.strip())
    linha = arq.readline()
    
  arq.close()


  for i in range (len(lst_site)):
    
    if lst_site[i][-2:] not in lst_domain:
      lst_domain.append(lst_site[i][-2:])
  
  print(lst_domain)

  cont=len(lst_domain)
  while cont<0:
    lst_aux=[]

    for j in range (len(lst_site)):

      if lst_site[-2:] ==lst_domain:
        lst_aux.append(lst_site)
      print(lst_aux)
    lst_d.append((lst_domain,lst_aux))

  print(lst_d)

  return(lst_d)


'''b) Construa a função relatorioDomains(<nome do arquivo>,<lista D>): <lista D>. A
função deve criar um arquivo de saída (escrita) de nome igual ao conteúdo do
primeiro parâmetro. O conteúdo do arquivo vem do processamento da lista D no
segundo parâmetro. A organização deste arquivo está expressa na figura 1.c. O
arquivo deve ser escrito linha a linha (write()). O arquivo deve ser fechado antes do
término da função. A função retorna como saída a mesma lista D recebida como
segundo parâmetro.'''

#def relatorioDomains(nomearq,lst_d):









'''c) Construa a função main() para executar o seguinte processamento: Main deve
chamar a função do item (a) para processar o arquivo webdomains.txt e retornar
uma lista D. Em seguida, main de chamar a função do item (b) para criar um
arquivo chamado saidaprova1.txt a partir da lista D retornada pela chamada à
função processa(..).'''

def main():
  lst_d=[]
  
  lst_d=(processa("webdomains"))

  #relatorioDomains(webdomains,lst_d)
  
if __name__ == "__main__":
  main()