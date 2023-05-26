import json

def main():
  data_JSON =  """
  {
  	"size": "Medium",
  	"price": 15.67,
  	"toppings": ["Mushrooms", "Extra Cheese", "Pepperoni", "Basil"],
  	"client": {
  		"name": "Jane Doe",
  		"phone": "455-344-234",
  		"email": "janedoe@email.com"
  	}
  }
  """
  # Converter a string em JSON em um dicionário
  data_dict = json.loads(data_JSON)

  print(data_JSON)
  print()
  print(data_dict)
  print("\n")
  print(data_dict["size"])
  print(data_dict["price"])
  print(data_dict["toppings"])
  print(data_dict["client"])

main()