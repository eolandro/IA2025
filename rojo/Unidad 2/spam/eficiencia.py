from ruamel.yaml import YAML

yaml = YAML()

def cargar_mensajes(archivo):
    with open(archivo, 'r') as file:
        data = yaml.load(file)
        return data['MensajesClasificados']

def preguntar_usuario(mensajes):
    respuestas_usuario = []
    for item in mensajes:
        mensaje = item['mensaje']
        while True:
            respuesta = input(f"\n¿Este mensaje es spam? (si/no): \n'{mensaje}'\n").lower()
            if respuesta in ['si', 'no']:
                respuestas_usuario.append({'mensaje': mensaje, 'spam': respuesta == 'si'})
                break
    return respuestas_usuario

def comparar_respuestas(mensajes_originales, respuestas_usuario):
    spam_coincidencias = 0
    total_spam_usuario = 0
    total_spam_clasificador = 0

    for i in range(len(mensajes_originales)):
        etiqueta_original = mensajes_originales[i]['etiqueta']
        respuesta_usuario = 'spam' if respuestas_usuario[i]['spam'] else 'no_spam'

        if etiqueta_original == 'spam':
            total_spam_clasificador += 1
        if respuesta_usuario == 'spam':
            total_spam_usuario += 1
            if etiqueta_original == 'spam':
                spam_coincidencias += 1

    return spam_coincidencias, total_spam_usuario, total_spam_clasificador

def main():
    mensajes = cargar_mensajes('mensajesClasificar.yaml')
    respuestas_usuario = preguntar_usuario(mensajes)
    spam_coincidencias, total_spam_usuario, total_spam_clasificador = comparar_respuestas(mensajes, respuestas_usuario)

    total_corregido = total_spam_usuario - (total_spam_clasificador - spam_coincidencias)
    porcentaje_spam = (total_corregido / total_spam_usuario * 100) if total_spam_usuario > 0 else 0

    print(f"\nTotal de mensajes spam {total_spam_clasificador}")
    print(f"Coincidencias de spam: {spam_coincidencias} de {total_spam_usuario}")
    print(f"Porcentaje de eficiencia: {porcentaje_spam}%")

if __name__ == "__main__":
    main()
