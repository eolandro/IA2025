from ruamel.yaml import YAML

yaml = YAML()


with open("tablaprob.yaml", 'r', encoding='utf-8') as entrada:
    Datos = yaml.load(entrada)

with open("msjclasif.yaml", 'r', encoding='utf-8') as entrada:
    dat = yaml.load(entrada)

probabilidades = Datos['probabilidades']

promedio_global = sum(probabilidades.values()) / len(probabilidades)

umbral_diferencia = 0.02 


for i, mensaje in enumerate(dat['mensajes']):
    palabras = mensaje.split()  
    probabilidades_mensaje = []

    for palabra in palabras:
        palabra_limpia = palabra.strip('¡!¿?.,')  
        if palabra_limpia.lower() in probabilidades:  
            probabilidad = probabilidades[palabra_limpia.lower()]
            probabilidades_mensaje.append(probabilidad)

   
    if probabilidades_mensaje:
        promedio_mensaje = sum(probabilidades_mensaje) / len(probabilidades_mensaje)
    else:
        promedio_mensaje = 0

    diferencia = abs(promedio_mensaje - promedio_global)

  
    if promedio_mensaje > promedio_global or diferencia <= umbral_diferencia:
        clasificacion = True  # Spam
    else:
        clasificacion = False  # No spam


    dat['mensajes'][i] = {mensaje: clasificacion}

with open("msjspam.yaml", 'w', encoding='utf-8') as salida:
    yaml.dump(dat, salida)


print("\nMensajes clasificados:\n")
for i, mensaje in enumerate(dat['mensajes']):
    for texto, clasificacion in mensaje.items():
        print(f"Mensaje {i+1}: '{texto}' - {'Spam' if clasificacion else 'No Spam'}")


