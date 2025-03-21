from ruamel.yaml import YAML
yaml=YAML()
yaml.default_flow_style =False
yaml.indent(sequence=4, offset=2)

s=open("spam.yaml","r")
Data = yaml.load(s)
s.close()

emails = [i["mensaje"] for i in Data["emails"]]
spam_supuesto = Data["spam"]

total_spam=0
aciertos=0
for i in range(len(emails)):
    print(emails[i])
    if (int(input("¿Es Spam?Si(1)/No(0): "))):
        total_spam+=1
        if spam_supuesto[i]:
            aciertos+=1 
    print("*"*50)

eficiencia = aciertos/total_spam*100

print("La eficiencia del detector de spam es: "+str(eficiencia)+"%")