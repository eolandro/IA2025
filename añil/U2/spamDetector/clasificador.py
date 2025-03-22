import json
import unicodedata

def promedio(lista):
    if not lista:  
        return 0.0
    return sum(lista)/len(lista)

def normalizar(texto):
    texto = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('ascii')
    return texto.lower()

def deTokenizador(texto):    
    texto_normalizado = normalizar(texto)
    return texto_normalizado.split()

def probabilidad_spam(emails, tokens):
    probabilidades = []
    for email in emails:
        probs_email = []
        mensaje = deTokenizador(email["correo"])
        for palabra in mensaje:
            if palabra in tokens:
                probs_email.append(tokens[palabra])
        probabilidades.append(promedio(probs_email))
    return probabilidades

def es_spam(probabilidades):
    return [1 if p > 0.5 else 0 for p in probabilidades]

# Carga de archivos
with open("messagesx.json", 'r', encoding="utf-8") as file, \
     open("tokens_probabilidad.json", 'r', encoding="utf-8") as file2:

    data = json.load(file)
    emails = data["messages"]
    tokens_data = json.load(file2)
    tokens = tokens_data  

# Procesamiento
probabilidades = probabilidad_spam(emails, tokens)
lista_spam = es_spam(probabilidades)

nueva_data = {"messages": []}
for email, es_spam in zip(emails, lista_spam):
    nueva_data["messages"].append({
        "correo": email["correo"],
        "categoria": "spam" if es_spam else "normal"
    })

# Guardado de resultados
with open("clasified_spam.json", 'w', encoding="utf-8") as file:
    json.dump(nueva_data, file, ensure_ascii=False, indent=2)

print("-- Clasificación guardada correctamente --")
