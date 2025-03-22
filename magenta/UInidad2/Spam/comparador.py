from ruamel.yaml import YAML

yaml = YAML()
Datos = False
resul = []

# Cargar los datos desde msjspam.yaml
with open("msjspam.yaml", 'r', encoding='utf-8') as entrada:
    Datos = yaml.load(entrada)

# Preguntar al usuario sobre cada mensaje
for i, msj in enumerate(Datos['mensajes']):
    if isinstance(msj, dict):
        mensaje_texto = list(msj.keys())[0]
    else:
        mensaje_texto = msj

    R = input(f'\n El Mensaje: "{mensaje_texto}" es Spam? (s/n) => ')
    if R.lower() == 's':
        resul.append({mensaje_texto: True})
    else:
        resul.append({mensaje_texto: False})

# Mostrar resultados del supervisor
print("\n" + "=" * 30)
print("     Supervisor    ")
print("=" * 30,"\n")

for item in resul:
    mensaje, es_spam = list(item.items())[0]
    clasificacion = 'SPAM' if es_spam else 'NO SPAM'
    print(f'Mensaje: "{mensaje}" - Clasificaci\u00f3n: {clasificacion}')

# Mostrar resultados del clasificador
print("\n" + "=" * 30)
print("     Clasificador    ")
print("=" * 30,"\n")

for msj in Datos['mensajes']:
    if isinstance(msj, dict):
        mensaje_texto, valor = list(msj.items())[0]
        clasificacion = "SPAM" if valor else "NO SPAM"
        print(f'Mensaje: "{mensaje_texto}" - Clasificaci\u00f3n: {clasificacion}')

# Comparar los resultados
coincidencias = 0

for i, msj in enumerate(Datos['mensajes']):
    if isinstance(msj, dict):
        mensaje_texto, valor_original = list(msj.items())[0]  
    else:
        mensaje_texto = msj
        valor_original = False  
    valor_resul = resul[i][mensaje_texto] 
    if valor_resul == valor_original:
        coincidencias += 1

print("\n" + "=" * 10)
print(" Comparaci\u00f3n de resultados ")
print("=" * 10,"\n")
print(f'El n\u00famero de coincidencias es: {coincidencias}')
print(f'Total de mensajes comparados: {len(Datos["mensajes"])}')
