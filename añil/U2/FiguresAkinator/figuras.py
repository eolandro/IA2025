from ruamel.yaml import YAML

def cargar_datos(archivo):
    yaml = YAML(typ='safe')
    with open(archivo, 'r', encoding='utf-8') as f:
        return yaml.load(f)

def inicializar_condiciones():
    return [
        # Pregunta 0: ¿Tiene bordes redondos?
        lambda fig: fig in {'círculo', 'óvalo'},
        # Pregunta 1: ¿Es como una pelota?
        lambda fig: fig == 'círculo',
        # Pregunta 2: ¿Tiene 3 lados?
        lambda fig: fig.startswith('triángulo'),
        # Pregunta 3: ¿Tiene 4 lados?
        lambda fig: fig in {'cuadrado', 'rectángulo', 'rombo', 'trapecio', 'paralelogramo'},
        # Pregunta 4: ¿Tiene 6 lados?
        lambda fig: fig == 'hexágono',
        # Pregunta 5: ¿Tiene 10 lados?
        lambda fig: fig == 'decágono',
        # Pregunta 6: ¿Todos los lados son iguales?
        lambda fig: fig in {'triángulo equilátero', 'cuadrado', 'rombo'},
        # Pregunta 7: ¿Unir dos forma cuadrado/rectángulo?
        lambda fig: fig == 'triángulo rectángulo',
        # Pregunta 8: ¿Solo dos lados iguales?
        lambda fig: fig == 'triángulo isósceles',
        # Pregunta 9: ¿Dos pares de lados iguales?
        lambda fig: fig in {'rectángulo', 'paralelogramo'},  # Corregido para incluir ambos
        # Pregunta 10: ¿Parece diamante/cometa?
        lambda fig: fig == 'rombo',
        # Pregunta 11: ¿Está inclinada?
        lambda fig: fig == 'paralelogramo'  # Pregunta clave para diferenciar
    ]

def obtener_respuesta(pregunta):
    while True:
        respuesta = input(f"{pregunta} (sí/no): ").strip().lower()
        if respuesta in ('sí', 'si', 's'):
            return True
        elif respuesta in ('no', 'n'):
            return False
        else:
            print("Por favor, responde 'sí' o 'no'.")

def main():
    datos = cargar_datos('preguntas.yaml')
    figuras = datos['figuras']
    preguntas = datos['preguntas']
    condiciones = inicializar_condiciones()
    
    candidatos = figuras.copy()
    
    for i, (pregunta, condicion) in enumerate(zip(preguntas, condiciones)):
        if len(candidatos) <= 1:
            break  # Si ya hay una sola opción, terminar
        
        posibles_yes = [fig for fig in candidatos if condicion(fig)]
        posibles_no = [fig for fig in candidatos if not condicion(fig)]
        
        if not posibles_yes or not posibles_no:
            continue  # Pregunta no útil
        
        respuesta = obtener_respuesta(pregunta)
        candidatos = posibles_yes if respuesta else posibles_no
    
    # Verificar si quedan dudas entre rectángulo y paralelogramo
    if len(candidatos) == 2 and {'rectángulo', 'paralelogramo'}.issubset(candidatos):
        respuesta = obtener_respuesta("¿La figura está inclinada?")
        candidatos = ['paralelogramo'] if respuesta else ['rectángulo']
    
    if len(candidatos) == 1:
        print(f"¡La figura que estás pensando es un {candidatos[0]}!")
    else:
        print("No pude adivinar la figura. ¿Podrías decirme cuál era?")

if __name__ == "__main__":
    main()
