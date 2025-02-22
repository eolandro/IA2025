from analizarls import validarLinea, esEtiquetaValida
from pathlib import Path
from BoomeVM import BoomeVM
import argparse

parser = argparse.ArgumentParser(
    prog='Boom-e',
    description='Ejecuta instrucciones almacenadas de un archivo',
    epilog='Creado para no morir en el semestre'
)
parser.add_argument('archivo_codigo')

def ejecutarPrograma(archivo_codigo):
    with archivo_codigo.open() as codigo:
        maquinaVirtual = BoomeVM()
        print(maquinaVirtual)
        lineasCodigo = codigo.readlines()

        for indice, linea in enumerate(lineasCodigo):
            linea = linea.strip()
            if esEtiquetaValida(linea):
                maquinaVirtual.etiquetas[linea[:-1]] = indice

        indiceActual = 0
        while indiceActual < len(lineasCodigo) and maquinaVirtual.estaVivo:
            linea = lineasCodigo[indiceActual].strip()
            print("\n")
            resultado = validarLinea(linea)
            print(resultado)
            if resultado:
                indiceActual = maquinaVirtual.procesarInstruccion(linea, lineasCodigo, indiceActual)
                print(maquinaVirtual)
            else:
                indiceActual += 1
            input("Presiona ENTER para continuar...")

if __name__ == "__main__":
    args = parser.parse_args()
    ruta = Path(args.archivo_codigo)
    if ruta.exists():
        ejecutarPrograma(ruta)
    else:
        print("No se encontró el archivo especificado", args.archivo_codigo)