from ruamel.yaml import YAML

def recolectar_datos():
    datos = {"animales": [], "caracteristicas": []}
    print("\nBienvenido, vamos a recolectar información sobre animales\n")

    # Recolectar animales
    print("Comencemos con los animales. Si no deseas agregar más, simplemente presiona Enter.")
    while True:
        animal = input(f"Ingrese el nombre del animal (o presiona Enter para terminar): ").strip()
        if not animal:  # Si la entrada está vacía, terminamos la recopilación
            break
        if animal not in datos["animales"]:  # Verificar que no se repitan los animales
            datos["animales"].append(animal)
        else:
            print("Este animal ya ha sido ingresado, por favor ingresa uno diferente.")

    # Recolectar características
    print("\nAhora ingrese las características de los animales. Para terminar, presiona Enter.")
    while True:
        caracteristica = input(f"Ingrese una característica (o presiona Enter para terminar): ").strip()
        if not caracteristica:  # Si la entrada está vacía, terminamos la recopilación
            break
        datos["caracteristicas"].append(caracteristica)

    # Guardar los datos en un archivo YAML
    try:
        yaml = YAML()
        with open("preguntas_animales.yaml", "w") as archivo:
            yaml.dump(datos, archivo)
        print("Datos guardados exitosamente en preguntas_animales.yaml")
    except Exception as e:
        print(f"Ocurrió un error al guardar los datos: {e}")

if __name__ == "__main__":
    recolectar_datos()
