from ruamel.yaml import YAML
import os

yaml = YAML()

# Rutas de archivo
ruta_entrada = "C:/Users/ramir/Downloads/Ultimo Semestre/IA/Animales/PreguntasAnimales.yaml"
ruta_salida = "C:/Users/ramir/Downloads/Ultimo Semestre/IA/Animales/Tabla.yaml"

# Verificar si el archivo PreguntasAnimales.yaml existe
if not os.path.exists(ruta_entrada):
    print(f"El archivo {ruta_entrada} no existe. Asegúrate de crearlo primero.")
    exit()

# Cargar el archivo YAML de entrada
with open(ruta_entrada, 'r', encoding='utf-8') as entrada:
    Datos = yaml.load(entrada)

# Verificar que existan las claves necesarias
if 'Animales' not in Datos or 'Caracteristicas' not in Datos:
    print("El archivo PreguntasAnimales.yaml debe contener las secciones 'Animales' y 'Caracteristicas'.")
    exit()

# Extraer características y animales
L_carac = Datos['Caracteristicas']
animales = Datos['Animales']

data = {
    "encabezado": ["Animal"] + L_carac + ["Total"],
    "filas": []
}

for animal in animales:
    nombre_animal = animal.capitalize()  # Convertir el nombre a la primera letra mayúscula
    caracteristicas = {}

    for carac in L_carac:
        respuesta = input(f"¿El animal '{nombre_animal}' tiene la característica '{carac}'? (s/n) => ")
        if respuesta.lower() == 's':
            caracteristicas[carac] = 1
        else:
            caracteristicas[carac] = 0

    # Crear la representación binaria de las características
    total_str = ''.join(str(caracteristicas[carac]) for carac in L_carac)

    # Añadir el animal a la tabla de datos
    data['filas'].append({
        'nombre': nombre_animal,
        'caracteristicas': caracteristicas,
        'Total': total_str
    })

# Guardar los datos en un archivo YAML de salida
with open(ruta_salida, 'w', encoding='utf-8') as salida:
    yaml.dump(data, salida)

print(f"Archivo {ruta_salida} creado correctamente.")
