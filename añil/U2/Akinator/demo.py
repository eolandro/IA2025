from ruamel.yaml import YAML

s = open("ejemplo0.yaml", "w")

yaml = YAML()
yaml.default_flow_style = False

L = []
for a in range(3):
    L.append(input("Ingrea un animal: >"))

yaml.dump({'animales':  L}, s)
s.close()


#cargar a un yaml
s = open("ejemplo0.yaml", "r")
Data = yaml.load(s)
s.close()

print(Data,type(Data))
print(Data['animales'],type(Data['animales']))
print(Data['animales'][0],type(Data['animales'][0]))



import json

Lista = [
    ["Nivel 1", "Canción"],
    ["Nivel 2", "Pinguinos"],
    ["Nivel 3", "Retoño"]
]
print(json.dumps(Lista))
with open("data.json","w") as data:
    data,write(json.dumps(Lista))


with open("data.json","r") as data:
    r = json.load(data)
    print(r)


