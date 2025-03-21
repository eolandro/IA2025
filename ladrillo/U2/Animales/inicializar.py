import yaml
from unidecode import unidecode

# Ruta donde se guardará el archivo YAML
ruta_yaml = "C:/Users/ramir/Downloads/Ultimo Semestre/IA/Animales/PreguntasAnimales.yaml"

# Función para corregir texto con caracteres corruptos específicos
def corregir_texto(texto):
    texto = unidecode(texto)  # Convertir caracteres especiales a ASCII
    # Reemplazar caracteres corruptos específicos
    texto = texto.replace('A+-', 'ñ').replace('A!', 'á').replace('A3n', 'ón')
    return texto

# Crear el diccionario base para el archivo YAML
data = {
    "Caracteristicas": [],
    "Animales": []
}

# Obtener características del usuario
while True:
    caracteristica = input("Introduce una característica (o 'fin' para terminar): ").strip()
    if caracteristica.lower() == 'fin':
        break
    data["Caracteristicas"].append(corregir_texto(caracteristica))

# Obtener animales del usuario
while True:
    animal = input("Introduce el nombre de un animal (o 'fin' para terminar): ").strip()
    if animal.lower() == 'fin':
        break
    animal_corregido = corregir_texto(animal)
    
    # Verificar si el animal ya existe
    if animal_corregido in data["Animales"]:
        print(f"El animal '{animal_corregido}' ya está registrado.")
    else:
        data["Animales"].append(animal_corregido)

# Guardar los datos en un archivo YAML
with open(ruta_yaml, 'w', encoding='utf-8') as file:
    yaml.dump(data, file, allow_unicode=True)

print("Los datos han sido guardados en el archivo YAML.")
