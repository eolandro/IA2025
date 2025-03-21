from ruamel.yaml import YAML

def cargar_datos(archivo):
    yaml = YAML()
    with open(archivo, "r", encoding="utf-8") as file:
        return yaml.load(file)

def cargar_tabla_animales():
    return cargar_datos("Tabla.yaml").get("Animales", {})

def cargar_preguntas_animales():
    data = cargar_datos("PreguntasAnimales.yaml")
    return data.get("Animales", []), data.get("Preguntas", [])

def seleccionar_pregunta(animales_posibles, tabla_animales, preguntas):
    if not animales_posibles:
        return None, None

    for pregunta in preguntas:
        caracteristica = pregunta.split()[-1].capitalize()
        valores = [tabla_animales[animal].get(caracteristica, 0) for animal in animales_posibles]
        frecuencia_si = sum(valores)
        frecuencia_no = len(valores) - frecuencia_si

        if frecuencia_si > 0 and frecuencia_no > 0:
            return pregunta, caracteristica

    return None, None

def obtener_respuesta(pregunta):
    respuesta = input(f"\n¿{pregunta}? (s/n) => ").strip().lower()
    while respuesta not in ["s", "n"]:
        print("Respuesta no válida. Responde con 's' o 'n'.")
        respuesta = input(f"\n¿{pregunta}? (s/n) => ").strip().lower()
    return respuesta == "s"

def adivina_quien():
    animales, preguntas = cargar_preguntas_animales()
    tabla_animales = cargar_tabla_animales()

    if not animales or not tabla_animales or not preguntas:
        print("Error: No se pudieron cargar los datos correctamente.")
        return

    print("\n¡¡¡Bienvenido al juego Adivina Quién!!!\n")
    print("Piensa en uno de los siguientes animales:\n")
    for animal in animales:
        print(f"+ {animal}")

    animales_posibles = set(animales)

    while len(animales_posibles) > 1:
        pregunta, caracteristica = seleccionar_pregunta(animales_posibles, tabla_animales, preguntas)
        if pregunta is None:
            break

        respuesta_binaria = obtener_respuesta(pregunta)
        animales_posibles = {animal for animal in animales_posibles if tabla_animales[animal].get(caracteristica) == respuesta_binaria}

    if len(animales_posibles) == 1:
        print(f"\n¡El animal en el que estás pensando es: {next(iter(animales_posibles))}!")
    elif len(animales_posibles) == 2:
        animal1, animal2 = animales_posibles
        if obtener_respuesta(f"El animal que estás pensando es {animal1}"):
            print(f"\n¡El animal en el que estás pensando es: {animal1}!")
        else:
            print(f"\n¡El animal en el que estás pensando es: {animal2}!")
    else:
        print("\nNo he podido adivinar el animal.")

if __name__ == "__main__":
    adivina_quien()