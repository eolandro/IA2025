from ruamel.yaml import YAML

yaml = YAML()

def cargar_mensajes(archivo):
    with open(archivo, 'r') as file:
        data = yaml.load(file)
        return data['Mensajes']

def etiquetar_mensajes(mensajes):
    etiquetados = []
    for mensaje in mensajes:
        while True:
            respuesta = input(f"\n¿Este mensaje es spam? (si/no): \n'{mensaje}'\n").lower()
            if respuesta in ['si', 'no']:
                etiquetados.append({'mensaje': mensaje, 'spam': respuesta == 'si'})
                break
    return etiquetados

def guardar_mensajes_etiquetados(mensajes_etiquetados, archivo):
    with open(archivo, 'w') as file:
        yaml.dump({'Mensajes': mensajes_etiquetados}, file)

def main():

    mensajes = cargar_mensajes('mensajes.yaml')
    mensajes_etiquetados = etiquetar_mensajes(mensajes)

    guardar_mensajes_etiquetados(mensajes_etiquetados, 'mensajeEtiquetado.yaml')
    print("Las respuestas se han guardado exitosamente")

if __name__ == "__main__":
    main()
