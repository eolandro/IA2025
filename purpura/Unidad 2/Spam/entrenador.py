from ruamel.yaml import YAML
yaml=YAML()
yaml.default_flow_style =False
yaml.indent(sequence=4, offset=2)

s=open("emails.yaml","r")
Data = yaml.load(s)
s.close()

emails = [i["mensaje"] for i in Data["emails"]]
respuestas = []

for i in emails:
    print(i)
    respuestas.append(int(input("¿Es Spam?Si(1)/No(0): ")))
    print("*"*50)

r = open("emails_tag.yaml","w")
yaml.dump({'mensajes':emails,'respuestas':respuestas},r)
r.close()

print("\nRespuestas guardadas en el archivo")