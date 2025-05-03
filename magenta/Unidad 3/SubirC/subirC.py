# crear_yaml.py
import yaml
import os

grafo = {
    'A': {'B': 2, 'C': 1, 'Z': 4},
    'B': {'D': 6},
    'C': {'E': 3, 'Z': 1},
    'Z': {'D': 7},
    'D': {'F': 5},
    'E': {'F': 1},
    'F': {'H': 2, 'G': 10},
    'G': {'I': 6},
    'H': {'G': 5},
    'I': {}
}

ruta_archivo = os.path.join(os.path.dirname(__file__), "grafo.yaml")

# Escribir el YAML
with open(ruta_archivo, "w") as file:
    yaml.dump(grafo, file)

print(f"Archivo 'grafo.yaml' creado correctamente en:\n{ruta_archivo}")