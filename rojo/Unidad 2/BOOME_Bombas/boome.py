from ruamel.yaml import YAML
import random

yaml = YAML()

def cargar_mapa(archivo):
    with open(archivo, 'r') as file:
        mapa = yaml.load(file)
    
    for clave in mapa:
        mapa[clave] = 'X'
    
    return mapa


def detector(valor):
    Vacias10 = [0,0,0,0,0,0,0,0,1,1]
    Bombas10 = [1,1,1,1,1,1,1,1,1,0]
    FN = random.choice(Vacias10)
    FP = random.choice(Bombas10)
    return FP if valor == 1 else FN

def calcular_bayes(Bombaenmuestra, casillas_restantes):
    Vacioenmuestra = 1 - Bombaenmuestra
    Bombareal = (0.9 * Bombaenmuestra) / ((Bombaenmuestra * 0.9) + (Vacioenmuestra * 0.2))
    return Bombareal

def generar_ruta(Casillas):
    filas = ['A', 'B', 'C', 'D', 'E']
    columnas = range(1, 11)
    ruta = []

    for fila in filas:
        if filas.index(fila) % 2 == 0:
            for columna in columnas:
                ruta.append(f"{fila}{columna}")
        else:
            for columna in reversed(columnas):
                ruta.append(f"{fila}{columna}")
    
    return ruta

def mover_robot(Casillas):
    ruta = generar_ruta(Casillas)
    total_casillas = len(Casillas)
    casillas_restantes = total_casillas
    desactivadores = 3

    print("Mapa inicial:")
    mostrar_mapa(Casillas)

    for casilla in ruta:
        valor = Casillas[casilla]
        print(f"Revisando {casilla}...")

        resultado = detector(valor)
        print(f"Resultado del detector para {casilla} => {resultado}")

        if resultado == 1:
            Bomba_en_muestra = 1 / casillas_restantes
            probabilidad_bomba = calcular_bayes(Bomba_en_muestra, casillas_restantes)
            print(f"Probabilidad inicial de bomba en {casilla} => {probabilidad_bomba:.6f}")

            pruebas_realizadas = 1
            while pruebas_realizadas < 3:
                nuevo_resultado = detector(valor)
                pruebas_realizadas += 1
                print(f"Nuevo resultado del detector en {casilla} (prueba {pruebas_realizadas}) => {nuevo_resultado}")
                
                if nuevo_resultado == 1:
                    probabilidad_bomba = calcular_bayes(probabilidad_bomba, casillas_restantes)
                    print(f"Probabilidad actualizada de bomba en {casilla}: {probabilidad_bomba:.6f}")

            if probabilidad_bomba >= 0.5 and desactivadores > 0:
                print(f"¡Alerta! Probabilidad alta de bomba en {casilla} => {probabilidad_bomba:.2f}")
                print(f"Usando un desactivador en {casilla}.")
                desactivadores -= 1
                Casillas[casilla] = 1
        else:
            Casillas[casilla] = 0

        casillas_restantes -= 1
        print("-" * 40)

        mostrar_mapa(Casillas)

        if desactivadores == 0:
            print("Se han agotado los desactivadores.")
            break

def mostrar_mapa(mapa):
    filas = ['A', 'B', 'C', 'D', 'E']
    columnas = range(1, 11)
    for fila in filas:
        fila_mapa = [mapa[f"{fila}{columna}"] for columna in columnas]
        print(f"{fila}: {' '.join(str(x) for x in fila_mapa)}")
    print("\n")

Casillas = cargar_mapa('mapa_bombas.yaml')
mover_robot(Casillas)