import json

def calcular_eficiencia():
    # Cargar datos clasificados automáticamente
    with open("clasified_spam.json", "r", encoding="utf-8") as f:
        data_clasificado = json.load(f)
    
    # Extraer predicciones
    mensajes = data_clasificado["messages"]
    spam_predicho = [1 if msg["categoria"] == "spam" else 0 for msg in mensajes]
    
    total_spam = 0
    aciertos = 0
    
    print("\n" + "="*50)
    print("EVALUACIÓN DE EFICIENCIA DEL CLASIFICADOR")
    print("="*50 + "\n")
    
    for i, mensaje in enumerate(mensajes, 1):
        print(f"Mensaje #{i}:")
        print(mensaje["correo"])
        print("\n" + "-"*50)
        
        # Obtener clasificación manual
        while True:
            try:
                respuesta = input("¿Es Spam? Y/n: ").strip().lower()
                if respuesta == "y":
                    respuesta = 1
                elif respuesta == "n":
                    respuesta = 0
                else:
                    raise ValueError 

                if respuesta not in [0, 1]:
                    raise ValueError
                break
            except ValueError:
                print("Error: Debes ingresar 1 o 0\n")
        
        if respuesta == 1:
            total_spam += 1
            if spam_predicho[i-1] == 1:  
                aciertos += 1
                
        print("\n" + "*"*50 + "\n")
    
    try:
        eficiencia = (aciertos / total_spam) * 100
    except ZeroDivisionError:
        eficiencia = 0.0
    
    print("\n" + "="*50)
    print(f"RESULTADOS FINALES:")
    print(f"- Total mensajes revisados: {len(mensajes)}")
    print(f"- Spam detectados por el usuario: {total_spam}")
    print(f"- Aciertos del clasificador: {aciertos}")
    print(f"- Eficiencia: {eficiencia:.2f}%")
    print("="*50)

if __name__ == "__main__":
    calcular_eficiencia()
