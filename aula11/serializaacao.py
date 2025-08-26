import json 

aluno = {"matricula": 2025001, "nome": "Carlos Silva", "curso": "ADS"}

#serializar
json_data = json.dumps(aluno)
print("serializado:", json_data)

#desserializar
obj = json.loads(json_data)
print("curso:", obj["curso"])
obj["nome"] = "Pedro pereira"
print("Novo nome:", obj["nome"])