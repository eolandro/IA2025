import yaml
import re


def cargar_yaml(filename: str):
    with open(filename, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def guardar_yaml(data, filename: str):
    with open(filename, "w", encoding="utf-8") as file:
        yaml.dump(data, file, default_flow_style=False, allow_unicode=True)


def procesar_mensaje(mensaje: str):
    mensaje = mensaje.lower()
    mensaje = re.sub(r'[\W_]+', ' ', mensaje)  # Elimina todo excepto letras y números
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


def clasificar_manual_mensajes(mensajes):
    resultados_supervisor = []
    for mensaje in mensajes:
        print(f"Mensaje: {mensaje}")
        while True:
            respuesta = input("¿Es spam? (sí/no): ").strip().lower()
            if respuesta in ["sí", "si", "no"]:
                etiqueta_usuario = "spam" if respuesta in ["sí", "si"] else "no spam"
                resultados_supervisor.append({
                    "mensaje": mensaje,
                    "etiqueta_usuario": etiqueta_usuario
                })
                break
            else:
                print("Respuesta no válida. Escribe 'sí' o 'no'.")
    return resultados_supervisor


def calcular_porcentaje_acierto(mensajes_clasificados, resultados_supervisor):
    total_mensajes = len(mensajes_clasificados)
    aciertos = 0
    for i in range(total_mensajes):
        if mensajes_clasificados[i]["etiqueta"] == resultados_supervisor[i]["etiqueta_usuario"]:
            aciertos += 1
    return (aciertos / total_mensajes) * 100


if __name__ == "__main__":
    tabla_prob = cargar_yaml('C:/Users/ramir/Downloads/Ultimo Semestre/IA/MsjSPAM/Tabla_Probabilidad.yaml')
    nuevos_mensajes = cargar_yaml('C:/Users/ramir/Downloads/Ultimo Semestre/IA/MsjSPAM/NuevosMensajes.yaml')

    # Clasificación automática
    mensajes_clasificados = clasificar_mensajes(tabla_prob, nuevos_mensajes)
    guardar_yaml(mensajes_clasificados, 'C:/Users/ramir/Downloads/Ultimo Semestre/IA/MsjSPAM/mensajesFinalesEtiquetados.yaml')

    # Clasificación manual
    resultados_supervisor = clasificar_manual_mensajes(nuevos_mensajes)
    guardar_yaml(resultados_supervisor, 'C:/Users/ramir/Downloads/Ultimo Semestre/IA/MsjSPAM/deTokenizador.yaml')

    # Calcular porcentaje de acierto
    porcentaje_acierto = calcular_porcentaje_acierto(mensajes_clasificados, resultados_supervisor)
    print(f"El porcentaje de acierto del clasificador es: {porcentaje_acierto:.2f}%")
