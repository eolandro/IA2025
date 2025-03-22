import random
from ruamel.yaml import YAML

yaml = YAML()

def tablero(filename):
    with open(filename, 'r') as file:
        return yaml.load(file)
def resultado(filename, data):
    with open(filename, 'w') as file:
        yaml.dump(data, file)
resultado_file = "resultado.yaml"
try:
    with open(resultado_file, 'r') as file:
        resultados = yaml.load(file) or {}
except FileNotFoundError:
    resultados = {}

t = tablero("tablero.yaml")
posiciones = [(fila, col) for fila in t for col in t[fila]]

if "movimientos" not in resultados:
    resultados["movimientos"] = []

prob_ini = 2.50  
inc_prob = 33.50 
prob_max = 100.00  

intentos = len(resultados["movimientos"])

prob_exp = prob_ini + (intentos * inc_prob)
if prob_exp > prob_max:
    prob_exp = prob_max

prob = [prob_exp if t [fila][col] == 1 else (100 - prob_exp) for fila, col in posiciones]

fila, col = random.choices(posiciones, weights=prob, k=1)[0]

estado = "bomba" if t[fila][col] == 1 else "seguro"

resultados["movimientos"].append({
    "posicion": f"{fila}{col}",
    "estado": estado,
    "prob_res": f"{prob_exp:.2f}%"})

resultado(resultado_file, resultados)

msj = (
    f"Te encuentras en la posición: {fila}{col}\n"
    f"El estado es: {estado}!!!\n"
    f"La probabilidad de explotar es de {prob_exp:.2f}%.\n")

print(msj)

if estado == "bomba":
    print("\n¡Has encontrado una bomba!\n KABOOM! BOOM! BOOM! \n CRASH! SMASH! FLASH! \n  BANG! BOOM! DASH! \n")
