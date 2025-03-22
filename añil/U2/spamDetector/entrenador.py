import json

# Cargar el archivo JSON en modo lectura
with open("messages.json", 'r', encoding="utf-8") as file:
    data = json.load(file)

# Verificamos que la clave correcta sea "messages"
if "messages" not in data:
    print("Error: No se encontró la clave 'messages' en el archivo JSON.")
    exit()

# Creamos una nueva estructura para almacenar los datos clasificados
nueva_data = {"messages": []}

# Recorrer los correos y pedir clasificación
for mensaje in data["messages"]:
    print(mensaje["correo"])
    x = input("¿Es spam? (Y/n): ").strip().lower()

    if x == "y":
        etiqueta = "spam"
    elif x == "n":
        etiqueta = "normal"
    else:
        exit("Error: Respuesta inválida.")
        

    nueva_data["messages"].append({"correo": mensaje["correo"], "categoria": etiqueta})

# Guardar los cambios en el archivo JSON
with open("clasified_messages.json", 'w', encoding="utf-8") as file:
    json.dump(nueva_data, file, indent=1, ensure_ascii=False)

print("-- Clasificación guardada correctamente --")

