from ruamel.yaml import YAML
s=open("ejemplo0.yaml","w")
yaml=YAML()
yaml.default_flow_style =False
L =[]
C = []
N = int(input("¿cuantos animales agregarás?: "))
for a in range(N):
    L.append(input("Dame un animal: "))
    C.append(input("Agrega una característica para un animal: "))
yaml.dump({'animales': L, 'caracteristicas': C}, s)

s.close()

doc = open("ejemplo0.yaml")
Data = yaml.load(doc)
doc.close()
print(Data['animales'],type(Data['animales']))
print(Data['animales'][0],type(Data['animales'][0]))

print(Data['caracteristicas'],type(Data['caracteristicas']))
print(Data['caracteristicas'][0],type(Data['caracteristicas'][0]))



