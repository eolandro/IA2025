from analizarls import linea_codigo
from boomieVM import BoomieVM
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(
    prog="Boom-e",
    description="Interpretador de boome",
    epilog="Creado para no morir en el semestre"
)

parser.add_argument(
    "archivo_codigo",
    help="El archivo que contiene el código a ejecutar"
)

def main(archivo_codigo):
    with archivo_codigo.open() as codigo:
        Boome = BoomieVM()
        print(Boome)

        buffer = [linea.strip() for linea in codigo if linea.strip()] 
        Boome.collect_labels(buffer) #registo de etiquetas

        while Boome.Vivo and Boome.PC < len(buffer):
            linea = buffer[Boome.PC] 

            linea = linea.strip()
            print(f"#: {linea}")
            R = linea_codigo(linea)
            print(f"Lexical and Syntactic Analysis: {R}")

            if R:
                Boome.ejecutar_linea(linea)
                if not linea.startswith("je,jne"):
                    Boome.PC += 1
                print(Boome)

            input("Presiona enter para continuar...")

        if not Boome.Vivo:
            print(" -- GAME LOSE --")


if __name__ == "__main__":
    args = parser.parse_args()
    ruta = Path(args.archivo_codigo)
    if ruta.exists():
        main(ruta)
    else:
        print(f"El archivo ( {ruta} ) no existe")
        exit(1)
