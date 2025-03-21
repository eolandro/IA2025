import yaml

# Mostrar mensaje de bienvenida
print("********************************")
print("     Clasificador de Figuras")
print("********************************")
print("\n        ¡Vamos a Adivinar\n")

# Cargar los datos del archivo YAML
with open("C:/Users/ramir/Downloads/Ultimo Semestre/IA/Figuras/figpyr.yaml", "r", encoding="utf-8") as file:
    data = yaml.safe_load(file)

arbol2 = data["arbol2"]
arbolpreguntas = data["arbolpreguntas"]

nodo_actual = "Z"

# Función para obtener opciones dinámicamente según el nodo actual
def obtener_opciones(nodo):
    return [item[1] for item in arbol2 if item[0] == nodo]

# Ciclo para procesar hasta encontrar una figura final
while True:
    # Buscar la pregunta correspondiente al nodo actual
    pregunta = next((item[1] for item in arbolpreguntas if item[0] == nodo_actual), None)
    
    # Obtener las opciones válidas para el nodo actual
    opciones = obtener_opciones(nodo_actual)
    
    # Mostrar la pregunta y las opciones disponibles
    respuesta = input(f"{pregunta} (Opciones: {', '.join(opciones)}): ").strip()
    
    # Verificar si la respuesta es válida
    while respuesta not in opciones:
        print("Respuesta no válida. Intenta de nuevo.")
        respuesta = input(f"{pregunta} (Opciones: {', '.join(opciones)}): ").strip()

    # Buscar el siguiente nodo basado en la respuesta del usuario
    siguiente = next((item[2] for item in arbol2 if item[0] == nodo_actual and item[1].lower() == respuesta.lower()), None)
    nodo_actual = siguiente
    
    # Verificar si hemos llegado a un nodo de respuesta final
    final = next((item[1] for item in arbolpreguntas if item[0] == nodo_actual), None)
    if final and not final.startswith("¿"):  # Respuesta final encontrada
        print(f"La figura es: {final}")
        break
