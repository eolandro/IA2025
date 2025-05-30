from analizarls import validarLinea, esEtiquetaValida
from pathlib import Path
from BoomeVM import BoomeVM
import argparse

parser = argparse.ArgumentParser(
    prog='Boom-e',
    description='Ejecuta instrucciones del un archivo',
    epilog='Boome'
)
parser.add_argument('archivo_codigo')

def ejecutarPrograma(archivo_codigo):
    try:
        with archivo_codigo.open() as codigo:
            maquinaVirtual = BoomeVM()
            lineasCodigo = [linea.strip() for linea in codigo.readlines() if linea.strip()]
            
           
            for linea in lineasCodigo:
                if not validarLinea(linea):
                    print(f"Error de sintaxis en línea: {linea}")
                    return
            
            
            for indice, linea in enumerate(lineasCodigo):
                if esEtiquetaValida(linea):
                    maquinaVirtual.etiquetas[linea[:-1]] = indice
            
           
            indiceActual = 0
            while indiceActual < len(lineasCodigo) and maquinaVirtual.estaVivo:
                linea = lineasCodigo[indiceActual]
                print(f"\nEjecutando línea {indiceActual+1}: {linea}")
                
                indiceActual = maquinaVirtual.procesarInstruccion(linea, lineasCodigo, indiceActual)
                print(maquinaVirtual)
                
                if maquinaVirtual.estaVivo:
                    input("Presiona ENTER para continuar...")
                else:
                    print("¡El robot ha muerto!")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo_codigo}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    args = parser.parse_args()
    ruta = Path(args.archivo_codigo)
    if ruta.exists():
        ejecutarPrograma(ruta)
    else:
        print(f"No se encontró el archivo: {args.archivo_codigo}")