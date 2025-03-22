from ruamel.yaml import YAML

yaml = YAML()
Datos = False

with open("mensajes.yaml", 'r', encoding='utf-8') as entrada:
    Datos = yaml.load(entrada)

for i, msj in enumerate(Datos['mensajes']):
    R = input(f'¿El Mensaje: "{msj}" es Spam? (s/n) => ')
    if R.lower() == 's':
        Datos['mensajes'][i] = {msj: True}
    else:
        Datos['mensajes'][i] = {msj: False}


with open("msj1.yaml", 'w', encoding='utf-8') as salida:
    yaml.dump(Datos, salida)

print("\n" + "=" * 10)
print("     Mensajes Clasificados     ")
print("=" * 10,"\n")


