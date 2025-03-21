import re, string
from ruamel.yaml import YAML
yaml=YAML()
yaml.default_flow_style =False
yaml.indent(sequence=4, offset=2)

s=open("emails_tag.yaml","r")
Data = yaml.load(s)
s.close()

emails = Data["mensajes"]
respuestas = Data["respuestas"]
tokens_mails = []

signos = ".,?¿¡!:;"

# Lista de conjunciones, preposiciones y artículos comunes en español
palabras_a_eliminar = {
    "y", "o", "pero", "aunque", "sino", "porque", "que", "como", "cuando", "donde", "mientras",
    "de", "a", "en", "por", "para", "con", "sin", "sobre", "tras", "entre", "hasta", "desde",
    "el", "la", "los", "las", "un", "una", "unos", "unas", "tu", "te"
}

def deTokenizador(texto):    
    # Dividir el texto en palabras y filtrar las que están en la lista de eliminación
    palabras_filtradas = [palabra.lower().strip(signos) for palabra in texto.split() if palabra.lower() not in palabras_a_eliminar]
    
    # Volver a unir las palabras filtradas
    return palabras_filtradas

def tokenizador(tokens,mensajes,respuestas):
    dict = {}
    for t in tokens:
        cont_total = 0
        cont_spam = 0
        for i in range(len(mensajes)):
            if t in deTokenizador(mensajes[i]):
                cont_total+=1
                if respuestas[i]:
                    cont_spam+=1
        dict[t] = cont_spam/cont_total
    return dict


for i in emails:
    tokens_actuales = deTokenizador(i)
    for j in tokens_actuales:
        if j not in tokens_mails:
            tokens_mails.append(j)

print(tokens_mails)

tokens_prob = tokenizador(tokens_mails,emails,respuestas)

r = open("tokens.yaml","w")
yaml.dump({'tokens':tokens_prob},r)
r.close()