import yaml


def cargar_arbol(archivo):
    with open(archivo, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def normalizar_respuesta(respuesta):
    return respuesta.strip().lower()

def adivinar_figura(arbol):
    while True:  
        print("Piensa en una figura de la lista: cuadrado, rombo, romboide, trapecio, rectángulo,"
        "triangulo rectángulo, triagulo escaleno, triangulo equilátero, triangulo isósceles,circulo, elipse,"
        "pentagono, hexagono, decagono.\n")
        input("Presiona Enter cuando estés listo...")

        nodo = "A"  

        while "pregunta" in arbol[nodo]:
            print("\n" + arbol[nodo]["pregunta"])

      
            opciones = arbol[nodo]["respuestas"].keys()
            print(f"Opciones: {', '.join(opciones)}")


            respuesta_usuario = normalizar_respuesta(input("> "))


           
            respuestas_norm = {normalizar_respuesta(op): destino for op, destino in arbol[nodo]["respuestas"].items()}

           
            if respuesta_usuario in respuestas_norm:
                nodo = respuestas_norm[respuesta_usuario]
            else:
                print("⚠ Respuesta no válida, intenta de nuevo.")

       
        print(f"\n ¡Tu figura es: {arbol[nodo]['figura']}!\n")

       
        otra_figura = input("¿Quieres adivinar otra figura? (si/no): ").strip().lower()
        if otra_figura != "si":
            print("¡Gracias por jugar!")
            break  


if __name__ == "__main__":
    arbol = cargar_arbol("grafo.yaml")
    adivinar_figura(arbol)
