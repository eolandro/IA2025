import re, string
from ruamel.yaml import YAML
yaml=YAML()
yaml.default_flow_style =False
yaml.indent(sequence=4, offset=2)

s=open("emails_n.yaml","r")
Data = yaml.load(s)
s.close()

emails = Data["emails"]

r=open("tokens.yaml","r")
Data = yaml.load(r)
r.close()

tokens = Data["tokens"]

probabilidades = []

palabras_a_eliminar = {
    "y", "o", "pero", "aunque", "sino", "porque", "que", "como", "cuando", "donde", "mientras",
    "de", "a", "en", "por", "para", "con", "sin", "sobre", "tras", "entre", "hasta", "desde",
    "el", "la", "los", "las", "un", "una", "unos", "unas", "tu", "te"
}

def promedio(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma/len(lista)

def deTokenizador(texto):    
    # Dividir el texto en palabras y filtrar las que están en la lista de eliminación
    palabras_filtradas = [palabra.lower() for palabra in texto.split() if palabra.lower() not in palabras_a_eliminar]
    
    # Volver a unir las palabras filtradas
    return palabras_filtradas

def probabilidad_spam(emails,tokens):
    probabilidades = []
    for i in emails:
        probs_email = []  
        mensaje = deTokenizador(i["mensaje"])
        for j in tokens.keys():
            if j in mensaje:
                probs_email.append(tokens[j])
        probabilidades.append(promedio(probs_email))
    return probabilidades

def es_spam(probabilidades):
    spam = []
    for i in probabilidades:
        if i > 0.5:
            spam.append(1)
        else:
            spam.append(0)
    return spam

probabilidades = probabilidad_spam(emails,tokens)
lista_spam = es_spam(probabilidades)

t = open("spam.yaml","w")
yaml.dump({'emails':emails,'spam':lista_spam},t)
t.close()

for i in range(len(lista_spam)):
    es_spam = " no es spam"
    if lista_spam[i] == 1: 
        es_spam = " es spam"
    print("El correo "+str(i)+es_spam)