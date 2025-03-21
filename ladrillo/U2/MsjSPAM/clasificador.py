import yaml
import re

def cargar_yaml(filename: str):
    with open(filename, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)

def procesar_mensaje(mensaje: str):
    mensaje = mensaje.lower()
    mensaje = re.sub(r'[^\w\s]', '', mensaje)
    return mensaje.split()

def clasificar_mensajes(tabla_prob, mensajes):
    resultados = []
    for mensaje in mensajes:
        palabras = procesar_mensaje(mensaje)
        spam_probs = []
        no_spam_probs = []

        for palabra in palabras:
            palabra_upper = palabra.upper()
            if palabra_upper in tabla_prob:
                spam_probs.append(tabla_prob[palabra_upper]["probabilidad_spam"])
                no_spam_probs.append(tabla_prob[palabra_upper]["probabilidad_no_spam"])
            else:
                spam_probs.append(0.5)
                no_spam_probs.append(0.5)

        if spam_probs:
            prob_media_spam = sum(spam_probs) / len(spam_probs)
            prob_media_no_spam = sum(no_spam_probs) / len(no_spam_probs)
        else:
            prob_media_spam = prob_media_no_spam = 0.5

        etiqueta = "spam" if prob_media_spam > prob_media_no_spam else "no spam"

        resultados.append({
            "mensaje": mensaje,
            "probabilidad_media_spam": prob_media_spam,
            "probabilidad_media_no_spam": prob_media_no_spam,
            "etiqueta": etiqueta
        })
    return resultados

def guardar_yaml(data, filename: str):
    with open(filename, "w", encoding="utf-8") as file:
        yaml.dump(data, file, default_flow_style=False, allow_unicode=True)
