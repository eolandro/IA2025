import yaml

# Cargar los mensajes desde el archivo YAML
with open("C:/Users/ramir/Downloads/Ultimo Semestre/IA/MsjSPAM/Mensajes.yaml", "r", encoding="utf-8") as file:
    mensajes = yaml.safe_load(file)

# Lista para guardar los mensajes etiquetados
mensajes_etiquetados = []

# Etiquetar mensajes como spam o no spam
for mensaje in mensajes:
    print(f"\nMensaje: {mensaje}")
    etiqueta = input("¿Es spam? (si/no): ").strip().lower()
    
    if etiqueta == "si":
        etiqueta = "spam"
    elif etiqueta == "no":
        etiqueta = "no spam"
    else:
        print("Opción inválida. Se guardará como 'no spam'.")
        etiqueta = "no spam"

    mensajes_etiquetados.append({
        "mensaje": mensaje,
        "etiqueta": etiqueta
    })

# Guardar mensajes etiquetados en un nuevo archivo YAML
with open("C:/Users/ramir/Downloads/Ultimo Semestre/IA/MsjSPAM/mensajes_etiquetados.yaml", "w", encoding="utf-8") as file:
    yaml.dump(mensajes_etiquetados, file, allow_unicode=True)

print("\n¡Etiquetado completado! Se guardó en 'mensajes_etiquetados.yaml'.")
