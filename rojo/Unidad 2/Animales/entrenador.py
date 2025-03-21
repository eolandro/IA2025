from ruamel.yaml import YAML

yaml = YAML()

# * Carga los animales y las preguntas
with open("PreguntasAnimales.yaml", "r", encoding="utf-8") as file:
    data = yaml.load(file)

# * Obtener la lista de animales y preguntas
animales = data["Animales"]
preguntas = data["Preguntas"]

# * Tabla de bits (características)
num_preguntas = len(preguntas)
bits = {}

for i, pregunta in enumerate(preguntas):
    ultima_palabra = pregunta.split()[-1].capitalize()      # * Capitalize = "pico" > "Pico"
    bits[ultima_palabra] = 2 ** (num_preguntas - 1 - i)

print("\nTabla de Bits:")
for k, v in bits.items():
    print(f"{k}: {v}")

tabla_animales = {}

for animal in animales:
    print(f"\nAnimal: {animal}")
    caracteristicas = {}
    puntaje_total = 0

    for pregunta in preguntas:
        # * Muestra la pregunta y luego asigna un valor
        respuesta = input(f"¿{pregunta}? (s/n): ").strip().lower()
        valor = 1 if respuesta == "s" else 0

        # * Buscar la característica asociada a la última palabra de la pregunta
        caracteristica = pregunta.split()[-1].capitalize()

        # * Guarda la característica junto con su valor (0 o 1), además se calcula el puntaje total
        caracteristicas[caracteristica] = valor
        puntaje_total += bits[caracteristica] * valor

    # * Agregar el puntaje total al diccionario de características
    caracteristicas["Puntaje"] = puntaje_total

    # * Guardar el animal y sus características en la tabla
    tabla_animales[animal] = caracteristicas

# * Ordenar la tabla de animales por puntaje (de mayor a menor)
tabla_animales = dict(sorted(tabla_animales.items(), key=lambda x: x[1]["Puntaje"], reverse=True))

# * Escribe los datos en el archivo YAML
with open("Tabla.yaml", "w") as file:
    yaml.dump({"Animales": tabla_animales}, file)

print("\nTabla guardada en 'Tabla.yaml'")