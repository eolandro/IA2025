from ruamel.yaml import YAML

yaml = YAML()
yaml.default_flow_style = False

animales = []
preguntas = []

# * Solicitar preguntas y animales
print("Ingresa los animales\n")
for a in range(10):
    animales.append(input("Dame un animal: "))

print("\nIngresa las preguntas\n")
for b in range(10):
    preguntas.append(input("Escribe una pregunta (Sin colocar '¿?'): "))

# * Creación del diccionario
data = {
    'Animales': animales,
    'Preguntas': preguntas
}

# * Escribe los datos en el archivo YAML
with open("PreguntasAnimales.yaml", "w", encoding="utf-8") as file:
    yaml.dump(data, file)

print("\nDatos guardados en 'PreguntasAnimales.yaml'")