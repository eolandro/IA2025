from ruamel.yaml import YAML

class Nodo:
    def __init__(self, pregunta, respuestas):
        self.pregunta = pregunta
        self.respuestas = respuestas  # Lista de opciones posibles
        self.hijos = {}               # Diccionario {respuesta: Nodo o str}

def construir_arbol(data):
    figuras_validas = set(data['figuras'])
    
    def parsear_nodo(nodo_id):
        contenido = data[nodo_id]
        
        if 'figura' in contenido:
            # Nodo terminal (figura)
            figura = contenido['figura']
            if figura not in figuras_validas:
                raise ValueError(f"Figura no reconocida: {figura}")
            return figura
        
        # Nodo de pregunta
        pregunta = contenido['pregunta']
        respuestas = list(contenido['respuestas'].keys())
        nodo = Nodo(pregunta, respuestas)
        
        for respuesta, hijo_id in contenido['respuestas'].items():
            nodo.hijos[respuesta] = parsear_nodo(hijo_id)
        
        return nodo
    
    return parsear_nodo('A')

def obtener_respuesta(pregunta, opciones):
    print(f"\n{pregunta}")
    for i, opcion in enumerate(opciones):
        print(f"{chr(97 + i)}) {opcion}")
    
    while True:
        eleccion = input("Elige una opción (a, b, c...): ").lower()
        indice = ord(eleccion) - 97
        
        if 0 <= indice < len(opciones):
            return opciones[indice]
        print("Opción inválida. Intenta de nuevo.")

def recorrer_arbol(nodo_actual):
    if isinstance(nodo_actual, str):
        return nodo_actual
    
    respuesta = obtener_respuesta(nodo_actual.pregunta, nodo_actual.respuestas)
    
    if respuesta not in nodo_actual.hijos:
        print("Respuesta no reconocida. Intenta de nuevo.")
        return recorrer_arbol(nodo_actual)
    
    return recorrer_arbol(nodo_actual.hijos[respuesta])

def main():
    yaml = YAML(typ='safe')
    with open('grafo_figs.yaml', 'r', encoding='utf-8') as f:
        datos = yaml.load(f)
    
    print("Figuras disponibles:", ", ".join(datos['figuras']), "\n")
    
    arbol = construir_arbol(datos)
    resultado = recorrer_arbol(arbol)
    print(f"\n¡Tu figura es un {resultado}!")

if __name__ == "__main__":
    main()
