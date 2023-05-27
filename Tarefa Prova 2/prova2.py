import json

def veiculos_2_json(nomearq):
    lst = []
    dicc = {}
    arq = open(nomearq, "rt")
    for linha in arq:
        lista = linha.strip().split(", ")

        dicc = ({'Placa': lista[0],
                 'Modelo': lista[1],
                 'Marca': lista[2], 
                 'KM': int(lista[3])})

        lst.append(dicc)
    
    dicc_aux = {'Dados': lst}
    with open("bdveiculos.json", "w") as outfile:
        json.dump(dicc_aux, outfile,indent=4)

def props_2_json(nomearq):   
    lst = []
    dicc = {}
    arq = open(nomearq, "rt")
    for linha in arq:
        lista = linha.strip().split(";")

        dicc = ({'cpf': lista[0],
                 'nome': lista[1],
                 'end': lista[2], 
                 'celular': lista[3]})

        lst.append(dicc)
    
    dicc_aux = {'Dados': lst}
    with open("bdproprietarios.json", "w") as outfile:
        json.dump(dicc_aux, outfile,indent=4)

def json_to_dic_placas(nomearjson):
    with open(nomearjson) as json_file:
        x = json.load(json_file)
    carros = x["Dados"]
    dicc = {}
    for carro in carros:
        placa = carro["Placa"]
        carro.pop("Placa")
        dicc[placa] = carro
    return dicc 

def json_to_dic_cpfs(nomearjson):
    with open(nomearjson) as json_file:
        x = json.load(json_file)
    props = x["Dados"]
    dicc = {}
    for prop in props:
        cpf = prop["cpf"]
        prop.pop("cpf")
        dicc[cpf] = prop
    return dicc 

def json_to_json(nomearq):
    lst = []
    lst_aux = []
    dic_aux = {}
    with open(nomearq) as json_file:
        x = json.load(json_file)
    carros = x["Dados"]
    dicc = {}
    for carro in carros:
        marca = carro["Marca"]
        placa = carro["Placa"]
        if marca not in dicc:
            dicc[marca] = lst
        lst.append(placa)
        dicc[marca]= lst
    
    for id in dicc:
        dic_aux.update({id:dicc[id]})
        lst_aux.append(dic_aux)

    json_arq = {"dados" : lst_aux}
    
    with open("saida.json", "w") as outfile:
        json.dump(json_arq, outfile,indent=4)


def main():

   bdveiculos = "Tarefa Prova 2\\bdveiculos.csv"
   bdproprietarios = "Tarefa Prova 2\\bdproprietarios.csv"
   
   veiculos_2_json(bdveiculos)
   props_2_json(bdproprietarios)
   print(json_to_dic_placas("Tarefa Prova 2\\bdveiculos.json"))
   print(json_to_dic_cpfs("Tarefa Prova 2\\bdproprietarios.json"))
   json_to_json("Tarefa Prova 2\\bdveiculos.json")


main()