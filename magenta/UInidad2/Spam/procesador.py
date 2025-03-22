from ruamel.yaml import YAML

yaml = YAML()
Datos = False

with open("msj1.yaml", 'r', encoding='utf-8') as entrada:
    cad = entrada.read()
    Datos = yaml.load(cad)

mesj = []

for msj in Datos['mensajes']:
    for msje, val in msj.items():
        if val:
            mesj.append(msje)

for i in range(len(mesj)):
    texto = mesj[i].lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '')
   
    mesj[i] = [palabra for palabra in texto.split() if palabra.endswith(('ar', 'er', 'ir', 'ado', 'ido', 'oso', 'osa'))]


palabras_contadas = {}  
total_lineas = len(mesj)  

for lista_palabras in mesj:
    for palabra in lista_palabras:
        if palabra not in palabras_contadas:
          
            cuenta = sum([lista.count(palabra) for lista in mesj])
            
            promedio = cuenta / total_lineas
            palabras_contadas[palabra] = round(promedio, 4)

proba = {"probabilidades": palabras_contadas}

with open("tablaprob.yaml", 'w', encoding='utf-8') as salida:
    yaml.dump(proba, salida)

print("\n" + "=" * 10)
print("     Tabla generada     ")
print("=" * 10,"\n")
