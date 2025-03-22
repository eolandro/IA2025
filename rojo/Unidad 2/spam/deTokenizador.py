from collections import Counter
from ruamel.yaml import YAML
import string
import unicodedata

yaml = YAML()

palabras_descartar = {
    'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'a', 'ante', 'bajo', 'cabe', 'con', 
    'contra', 'de', 'desde', 'en', 'entre', 'hacia', 'hasta', 'para', 'por', 'según', 'sin', 
    'so', 'sobre', 'tras', 'y', 'o', 'ni', 'que', 'como', 'al', 'del'
}

def limpiar_mensaje(mensaje):

    palabras = mensaje.lower().translate(str.maketrans('', '', string.punctuation)).split()
    palabras_filtradas = [quitar_acentos(palabra) for palabra in palabras 
                          if palabra not in palabras_descartar and not palabra.isdigit()]
    return palabras_filtradas

def quitar_acentos(palabra):
    return ''.join(char for char in unicodedata.normalize('NFD', palabra) if unicodedata.category(char) != 'Mn')

def cargar_mensajes(archivo):
    with open(archivo, 'r') as file:
        data = yaml.load(file)
        return data.get('Mensajes', [])

#Funcion que hace la tabla de probabilidad, esta tiene un contador de spam y no spam que cuenta cuantas veces aparece esta palabra en cada mensaje
def generar_tabla_probabilidad(mensajes, media_spam=0.11):
    contador_spam = Counter()
    contador_no_spam = Counter()
    total_spam = total_no_spam = 0
    
    #Se encarga de limpiar el mensaje y dependiendo si es spam o si no es spam el mensaje actualiza el contador de las palabras que contenga
    for item in mensajes:
        palabras = limpiar_mensaje(item['mensaje'])
        if item.get('spam', False):
            contador_spam.update(palabras)
            total_spam += len(palabras)
        else:
            contador_no_spam.update(palabras)
            total_no_spam += len(palabras)
    
    #Se crea el diccionario y se van determinando las palabras totales
    tabla_probabilidad = {}
    palabras_totales = set(contador_spam.keys()).union(set(contador_no_spam.keys()))
    
    #Para cada palabra se verifica su probabilidad de spam y de no spam
    #Este calcula cuantas veces aparece la palabra tanto en spam como no spam y lo divide entre el total de palabras de cada uno
    for palabra in palabras_totales:
        prob_spam = (contador_spam[palabra] / total_spam * 100) if total_spam > 0 else 0.0
        prob_no_spam = (contador_no_spam[palabra] / total_no_spam * 100) if total_no_spam > 0 else 0.0
        
#Se calcula la probabilidad final de spam y al final se etiqueta por cada mensaje su probabilidad de spam y no spam
        prob_spam_final = prob_spam + media_spam
        tabla_probabilidad[palabra] = {
            'probabilidad_spam': round(prob_spam_final, 10),
            'probabilidad_no_spam': round(prob_no_spam, 10)
        }
    
    return tabla_probabilidad

def guardar_tabla_probabilidad(tabla, archivo):
    with open(archivo, 'w') as file:
        yaml.dump({'TablaProbabilidad': tabla}, file)

def main():

    mensajes = cargar_mensajes('mensajeEtiquetado.yaml')    
    tabla_probabilidad = generar_tabla_probabilidad(mensajes, media_spam=0.11)  
    guardar_tabla_probabilidad(tabla_probabilidad, 'tablaprobabilidad.yaml')

    print("Tabla de probabilidad guardada de forma correcta.")

if __name__ == "__main__":
    main()