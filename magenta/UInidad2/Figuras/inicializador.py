import yaml
import os

def identificar_figura():
    
    datos_yaml = {
        "Preguntas": {
            "0": ["Selecciona una opción (1. Redonda / 2. Alargada)"],
            "3": [
                "¿Los tres lados son iguales? (1. Sí / 2. No)",
                "¿Al menos dos lados son iguales? (1. Sí / 2. No)",
                "¿Tiene un ángulo de 90°? (1. Sí / 2. No)"
            ],
            "4": [
                "¿Tiene todos sus lados iguales? (1. Sí / 2. No)",
                "¿Sus ángulos son todos rectos (90°)? (1. Sí / 2. No)",
                "¿Tiene todos sus ángulos rectos? (1. Sí / 2. No)",
                "¿Tiene un par de lados paralelos? (1. Sí / 2. No)"
            ],
            "5": ["¿Tiene todos sus lados iguales? (1. Sí / 2. No)"],
            "6": ["¿Tiene todos sus lados iguales? (1. Sí / 2. No)"],
            "10": ["¿Tiene todos sus lados iguales? (1. Sí / 2. No)"]
        },
        "Figuras": [
            "Círculo", "Elipse", "Triángulo Equilátero", "Triángulo Isósceles",
            "Triángulo Rectángulo", "Triángulo Escaleno", "Cuadrado", "Rombo",
            "Rectángulo", "Trapecio", "Trapezoide", "Pentágono", "Hexágono", "Decágono"
        ]
    }

    
    ruta_yaml = os.path.join(os.path.dirname(__file__), "preguntas_organizadas.yaml")
    with open(ruta_yaml, "w", encoding="utf-8") as file:
        yaml.dump(datos_yaml, file, default_flow_style=False, allow_unicode=True)

    print(" El archivo 'preguntas_organizadas.yaml' ha sido creado correctamente.")

    
    respuestas = []
    lados = int(input("¿Cuántos lados tiene la figura? (0, 3, 4, 5, 6, 10): "))
    respuestas.append(f"¿Cuántos lados tiene la figura? {lados}")

    if lados == 0:
        forma = int(input("Selecciona una opción (1. Redonda / 2. Alargada): "))
        respuestas.append(f"Selecciona una opción: {forma}")
        resultado = "Círculo" if forma == 1 else "Elipse"

    elif lados == 3:
        equilatero = int(input("¿Los tres lados son iguales? (1. Sí / 2. No): "))
        respuestas.append(f"¿Los tres lados son iguales? {equilatero}")
        if equilatero == 1:
            resultado = "Triángulo Equilátero"
        else:
            isosceles = int(input("¿Al menos dos lados son iguales? (1. Sí / 2. No): "))
            respuestas.append(f"¿Al menos dos lados son iguales? {isosceles}")
            if isosceles == 1:
                resultado = "Triángulo Isósceles"
            else:
                rectangulo = int(input("¿Tiene un ángulo de 90°? (1. Sí / 2. No): "))
                respuestas.append(f"¿Tiene un ángulo de 90°? {rectangulo}")
                resultado = "Triángulo Rectángulo" if rectangulo == 1 else "Triángulo Escaleno"

    elif lados == 4:
        iguales = int(input("¿Tiene todos sus lados iguales? (1. Sí / 2. No): "))
        respuestas.append(f"¿Tiene todos sus lados iguales? {iguales}")
        if iguales == 1:
            angulos_rectos = int(input("¿Sus ángulos son todos rectos (90°)? (1. Sí / 2. No): "))
            respuestas.append(f"¿Sus ángulos son todos rectos? {angulos_rectos}")
            resultado = "Cuadrado" if angulos_rectos == 1 else "Rombo"
        else:
            angulos_rectos = int(input("¿Tiene todos sus ángulos rectos? (1. Sí / 2. No): "))
            respuestas.append(f"¿Tiene todos sus ángulos rectos? {angulos_rectos}")
            if angulos_rectos == 1:
                resultado = "Rectángulo"
            else:
                paralelos = int(input("¿Tiene un par de lados paralelos? (1. Sí / 2. No): "))
                respuestas.append(f"¿Tiene un par de lados paralelos? {paralelos}")
                resultado = "Trapecio" if paralelos == 1 else "Trapezoide"

    elif lados == 5:
        resultado = "Pentágono"
    elif lados == 6:
        resultado = "Hexágono"
    elif lados == 10:
        resultado = "Decágono"
    else:
        resultado = "Número de lados no válido o figura no incluida"

    respuestas.append(f"La figura es un {resultado}.")

    
    print(f"\n La figura es un {resultado}.")


identificar_figura()
