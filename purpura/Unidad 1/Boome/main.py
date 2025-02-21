from analizador import linea_codigo
from BoomeVM import BoomeVM
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(
    prog='Boom-e',
    description='Ejecuta instrucciones almacenadas en un archivo',
    epilog = 'Creado para no morir en el semestre'
)

parser.add_argument('archivo_codigo')
def main(archivo_codigo):
    with archivo_codigo.open() as archivo:
        codigo = archivo.read().split("\n")
        if codigo[-1] == "":
            codigo = codigo[:-1]
        cont = 0
        Boome = BoomeVM()
        print(codigo)
        print(Boome)
        while cont < len(codigo):
            linea = codigo[cont]
            if not Boome.Vivo:
                break
            linea = linea.strip()
            print("#: ",linea)
            R = linea_codigo(linea)
            print("Analizador",R)
            if R:
                Boome.ejectuar_linea(linea)
                print(Boome)
                if Boome.salto:
                    cont = codigo.index(Boome.salto+":")
                else:
                    cont+=1
            else:
                break
            input("Presiona enter para continuar...")

if __name__ == "__main__":
    args = parser.parse_args()
    ruta = Path(args.archivo_codigo)
    if ruta.exists():
        main(ruta)
    else:
        print("No se encongtró el archivo especificado: ",args.archivo_codigo)