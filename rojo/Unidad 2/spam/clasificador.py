from ruamel.yaml import YAML

yaml = YAML()

def cargar_tabla_probabilidad(archivo):
    with open(archivo, 'r') as file:
        data = yaml.load(file)
        return data['TablaProbabilidad']

def cargar_mensajes(archivo):
    with open(archivo, 'r', encoding='utf-8') as file:
        data = yaml.load(file)
        return data['Mensajes']

#Esta funcion se encarga de calcular la probabilidad del cada mensaje, yendo palabra por palabra
#primero definimos la probabilidad en 1 para empezar desde ahi
def calcular_probabilidad_mensaje(mensaje, tabla_probabilidad):
    palabras = mensaje.lower().split()
    prob_spam = 1.0
    prob_no_spam = 1.0 

#Despues quitamos cualquier caracter especial que llegara a afectar y vamos palabra por palabra verificando la probabilidad de spam y de no spam
    for palabra in palabras:
        palabra = palabra.strip(".,!\"'") 
        if palabra in tabla_probabilidad:
            prob_spam *= tabla_probabilidad[palabra]['probabilidad_spam']
            prob_no_spam *= tabla_probabilidad[palabra]['probabilidad_no_spam']

#Una vez calculada la probabilidad del mensaje de spam y no spam lo que hacemos es verificar que la probabilidad no quede en 0
#Si es que queda en 0 le damos un valor definido
    total_prob = prob_spam + prob_no_spam
    if total_prob > 0:
        prob_spam /= total_prob
        prob_no_spam /= total_prob
    else:
        prob_spam, prob_no_spam = 0.5, 0.5

#Si la probabilidad de spam supera el limite definido entonces se marca el mensaje como spam, de lo contrario se marca como no spam
#esto ya que la mayoria de mensajes de spam supera este limite, y la mayoria de mensajes no spam no lo supera
    limite = 0.9
    return 'spam' if prob_spam > limite else 'no_spam'

def etiquetar_mensajes(mensajes, tabla_probabilidad):
    resultados = []
    for mensaje in mensajes:
        etiqueta = calcular_probabilidad_mensaje(mensaje, tabla_probabilidad)
        resultados.append({'mensaje': mensaje, 'etiqueta': etiqueta})
    return resultados

def guardar_mensajes_etiquetados(mensajes_etiquetados, archivo):
    with open(archivo, 'w') as file:
        yaml.dump({'MensajesClasificados': mensajes_etiquetados}, file)

def main():

    tabla_probabilidad = cargar_tabla_probabilidad('tablaProbabilidad.yaml')
    mensajes = cargar_mensajes('mensajes2.yaml')

    mensajes_etiquetados = etiquetar_mensajes(mensajes, tabla_probabilidad)
    guardar_mensajes_etiquetados(mensajes_etiquetados, 'mensajesClasificar.yaml')

    print("Mensajes clasificados de manera correcta")

if __name__ == "__main__":
    main()
