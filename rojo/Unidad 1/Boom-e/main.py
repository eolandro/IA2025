from analizadorLS   import linea_codigo, dLabel
from boome_vm       import BoomeVM
from pathlib        import Path
import argparse
import sys

parser = argparse.ArgumentParser(
    prog='Boom-e',
    description='Ejecuta instrucciones almacenadas de un archivo',
    epilog='Creado para no morir en el semestre'
)
parser.add_argument('archivo_codigo')

def main(archivo_codigo):
    with archivo_codigo.open() as codigo:
        boome = BoomeVM()
        lineas_codigo = codigo.readlines()
        
        # * Lee y guarda las etiquetas
        indice = 0
        for linea in lineas_codigo:
            linea = linea.strip()
            print(linea)
            if dLabel(linea):
                boome.etiquetas[linea[:-1]] = indice
            indice += 1
        
        indice_actual = 0   
        print(boome)
        
        while indice_actual < len(lineas_codigo) and boome.Vivo:
            linea = lineas_codigo[indice_actual].strip()
            print("--------------------------------------")
            R = linea_codigo(linea)
            print(R)
            if R:
                indice_actual = boome.ejecutar_linea(linea, indice_actual)
                print(boome)
            else:
                sys.exit(f"¡Error en la línea {indice_actual + 1}: {linea}!")
            # input("Presiona enter para continuar...")
            
if __name__ == "__main__":
    args = parser.parse_args()
    ruta = Path(args.archivo_codigo)
    if ruta.exists():
        main(ruta)
    else:
        print("No se encontró el archivo especificado: ", args.archivo_codigo)
    # main()
