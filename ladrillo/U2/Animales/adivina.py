import yaml
from tabulate import tabulate
from unidecode import unidecode
import random

# Cargar el archivo YAML (Tabla)
with open('C:/Users/ramir/Downloads/Ultimo Semestre/IA/Animales/Tabla.yaml', encoding='utf-8') as entrada:
    Datos = yaml.safe_load(entrada)

# Función para corregir texto con caracteres especiales

def corregir_texto(texto):
    return unidecode(texto)

# Corregir el encabezado
encabezado = [corregir_texto(col) for col in Datos['encabezado']]

# Convertir las filas en una lista de tuplas (o diccionarios) para facilitar la ordenación
filas_convertidas = []
for fila in Datos['filas']:
    fila_corregida = {
        'nombre': corregir_texto(fila['nombre']),
        'caracteristicas': {corregir_texto(k): v for k, v in fila['caracteristicas'].items()},
        'Total': fila['Total']
    }
    fila_corregida['Total_valor'] = int(fila['Total'], 2)
    filas_convertidas.append(fila_corregida)

# Ordenar las filas por el valor entero de "Total" en orden descendente
filas_ordenadas = sorted(filas_convertidas, key=lambda x: x['Total_valor'], reverse=True)

# Crear una lista de filas para la tabla

tabla = []
for fila in filas_ordenadas:
    fila_tabla = [fila['nombre']]
    for carac in encabezado[1:-1]:
        fila_tabla.append(fila['caracteristicas'].get(carac, 0))
    fila_tabla.append(fila['Total'])
    tabla.append(fila_tabla)

# Mostrar la tabla
print(tabulate(tabla, headers=encabezado, tablefmt='grid'))

print('Escoge un animal')
matriz = [encabezado] + tabla

c = 1  # Empezamos en la primera característica
while c < len(encabezado) - 1:
    if len(matriz) == 2:  # Solo queda un animal
        print(f'El animal que escogiste es {matriz[1][0]}')
        break

    respuesta = input(f'¿El animal que escogiste tiene {encabezado[c]}? (s/n) => ')
    if respuesta.lower() == 's':
        matriz = [matriz[0]] + [fila for fila in matriz[1:] if fila[c] == 1]
    else:
        matriz = [matriz[0]] + [fila for fila in matriz[1:] if fila[c] == 0]

    if len(matriz) == 2:  # Si solo queda un animal
        print(f'El animal que escogiste es {matriz[1][0]}')
        break

    c += 1

if len(matriz) > 2:  # Si quedan varios animales
    print('Los animales que coinciden con tus respuestas son:')
    for fila in matriz[1:]:
        print(f'- {fila[0]}')
