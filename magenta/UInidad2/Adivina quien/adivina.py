from ruamel.yaml import YAML


def cargar_tabla():
    yaml = YAML()
    try:
        with open("tabla.yaml", "r") as archivo:
            return yaml.load(archivo)
    except FileNotFoundError:
        print("Error: El archivo 'tabla.yaml' no se encuentra.")
        return {}
    except Exception as e:
        print(f"Error al cargar el archivo YAML: {e}")
        return {}

def obtener_respuesta(pregunta):
    while True:
        respuesta = input(f"¿El animal tiene la característica '{pregunta}'? (S/N): ").strip().lower()
        if respuesta in ['s', 'n']:
            return respuesta
        else:
            print("Por favor, ingresa 'S' o 'N'.")

def hacer_preguntas(tabla):
    animales = list(tabla.keys())
    preguntas = list(next(iter(tabla.values())).keys()) 
    
    print("\nAnimales existentes a adivinar:")
    for animal in animales:
        print("*", animal) 
    print("\n¡Vamos a adivinar tu animal!\n")

    
    respuestas = {}
    animales_filtrados = animales[:]
    
    
    for pregunta in preguntas:
        if len(animales_filtrados) <= 1:
            break  # 
        
        respuesta = obtener_respuesta(pregunta)
        respuestas[pregunta] = 1 if respuesta == 's' else 0

        animales_filtrados = [
            animal for animal in animales_filtrados
            if tabla[animal].get(pregunta) == respuestas[pregunta]
        ]
        
        # Mostramos los animales restantes para dar una mejor retroalimentación al usuario
        print(f"Animales posibles después de esta pregunta: {', '.join(animales_filtrados)}")

    # Si solo queda un animal, lo mostramos como respuesta
    if len(animales_filtrados) == 1:
        print(f"\nEl animal que pensaste es: {animales_filtrados[0]}")
    else:
        # Si hay empate entre animales, los mostramos todos
        print("\nNo pude adivinar el animal con certeza, los posibles animales son:")
        for animal in animales_filtrados:
            print("- " + animal)
        # Opcionalmente, preguntar si el usuario quiere elegir entre ellos
        elegir = input("\n¿Puedes elegir uno de los siguientes animales? Escribe el nombre: ").strip()
        if elegir in animales_filtrados:
            print(f"¡Has elegido: {elegir}!")
        else:
            print("El animal elegido no está en la lista. Gracias por jugar.")


def main():
    while True:
        tabla = cargar_tabla()
        if not tabla:
            break
        hacer_preguntas(tabla)
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (S/N): ").strip().lower()
        if jugar_de_nuevo != 's':
            print("Gracias por jugar. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
