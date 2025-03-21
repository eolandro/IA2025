from ruamel.yaml import YAML
yaml = YAML()
yaml.default_flow_style = None 

s = open("ejemplo0.yaml", "r")
Data = yaml.load(s)
s.close()


respuestas = {'animales': Data['animales'], 'caracteristicas': Data['caracteristicas'], 'respuestas': []}

bit_values = [2**(len(Data['caracteristicas']) - i - 1) for i in range(len(Data['caracteristicas']))]

def pedir_respuesta(animal, caracteristica):
    while True:
        respuesta = input(f"¿El/la {animal} {caracteristica}? (si/no): ").strip().lower()
        if respuesta == 'si':
            return 1
        elif respuesta == 'no':
            return 0
        else:
            print("Respuesta no válida. Por favor, responde con 'si' o 'no'.")
animales_bits = {}


for i in range(len(Data['animales'])):
    print(f"\nRespuestas para el animal: {Data['animales'][i]}")
    

    animal_respuestas_bits = []
    total_bits = 0  

    for j in range(len(Data['caracteristicas'])):
        caracteristica = Data['caracteristicas'][j]
        respuesta = pedir_respuesta(Data['animales'][i], caracteristica)
        

        if respuesta == 1:
            animal_respuestas_bits.append(1)  
            total_bits += bit_values[j] 
        else:
            animal_respuestas_bits.append(0)  
    respuestas['respuestas'].append(animal_respuestas_bits)
    
    animales_bits[Data['animales'][i]] = total_bits
animales_bits = dict(sorted(animales_bits.items(), key=lambda item: item[1], reverse=True))

s = open("respuestas.yaml", "w")
yaml.dump({'respuestas': respuestas, 'animales_bits': animales_bits}, s)
s.close()

print("\nLas respuestas se han guardado en 'respuestas.yaml'.")
