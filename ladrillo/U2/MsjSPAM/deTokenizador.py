import yaml
from collections import defaultdict
import re

# Listas de palabras a remover (sin duplicados)
preposiciones = {"a", "ante", "bajo", "cabe", "con", "contra", "de", "desde", "durante", "en", "entre", "hacia",
                 "hasta", "mediante", "para", "por", "según", "sin", "so", "sobre", "tras", "versus", "vía", 
                 "después de", "delante de", "debajo de"}
articulos = {"el", "la", "los", "las", "un", "una", "unos", "unas", "lo", "este", "esta", "ese", "esa"}
conjunciones = {"si", "como", "para que", "a fin de que", "que", "luego que", "mientras", "aunque", "si bien",
                "luego", "porque", "pues", "si", "o", "u", "pero", "sino", "si no", "y", "e", "ni", "lo mismo que", 
                "así como", "lo mismo", "ya que", "dado que", "puesto que", "visto que", "a causa de que", 
                "a causa de", "aunque", "mientras que"}

# Cargar mensajes etiquetados
with open("C:/Users/ramir/Downloads/Ultimo Semestre/IA/MsjSPAM/mensajes_etiquetados.yaml", "r", encoding="utf-8") as file:
    mensajes_etiquetados = yaml.safe_load(file)

# Contador de frecuencia de palabras
tabla_frecuencia = defaultdict(lambda: {"spam": 0, "no_spam": 0})
total_spam = 0
total_no_spam = 0

for mensaje_etiquetado in mensajes_etiquetados:
    mensaje = mensaje_etiquetado["mensaje"].lower()
    etiqueta = mensaje_etiquetado["etiqueta"]
    mensaje = re.sub(r'[^\w\s]', '', mensaje)  # Eliminar puntuación
    palabras = [p for p in mensaje.split() if p not in preposiciones and p not in articulos and p not in conjunciones]

    if etiqueta == "spam":
        total_spam += 1
        for palabra in palabras:
            tabla_frecuencia[palabra.upper()]["spam"] += 1
    elif etiqueta == "no spam":
        total_no_spam += 1
        for palabra in palabras:
            tabla_frecuencia[palabra.upper()]["no_spam"] += 1

# Generar tabla de probabilidades
probabilidad_default = 0.5

tabla_probabilidad = {
    palabra: {
        "probabilidad_spam": frecuencias["spam"] / total_spam if total_spam > 0 else probabilidad_default,
        "probabilidad_no_spam": frecuencias["no_spam"] / total_no_spam if total_no_spam > 0 else probabilidad_default
    }
    for palabra, frecuencias in tabla_frecuencia.items()
}

# Guardar la tabla de probabilidades
with open("C:/Users/ramir/Downloads/Ultimo Semestre/IA/MsjSPAM/Tabla_Probabilidad.yaml", 'w', encoding="utf-8") as file:
    yaml.dump(tabla_probabilidad, file, default_flow_style=False, allow_unicode=True)

print("Entrenamiento completado y tabla de probabilidades generada.")
