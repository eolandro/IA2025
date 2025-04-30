import json

def subircolina(inicio, fin):
    """
    algoritmo subircolina (camino mas corto)
    si se cicla regresa el recorrido aunque no 
    se haya llegado al destino
    """
    f = open('grafo.json','r')
    grafo = json.load(f)
    f.close()
    grafo = grafo["nodes"]
     
    last_position = ""
    position = inicio
    recorrido = []
    shorter = None

    while position != fin:

        if position in recorrido:
            print("-- Se cicló --")
            recorrido += [position] 
            break 

        recorrido += [position] 
        connections_init = grafo[position]["connection"]
        connections = [x for x in connections_init if x[0] != last_position]

        for node_c in connections:
            if not shorter :
                shorter = node_c
            elif node_c[1] < shorter[1]:
                shorter = node_c
        last_position = position
        position = shorter[0]
        shorter = None

    return recorrido 

#Repl
#Read eval print loop

def evaluation():
    while True:
        cmd = (input("> ").strip())
        if cmd == 'q':
            break
        try:
            print(eval(cmd))
        except Exception:
            pass

def main():
    evaluation()
    # recorrido = subircolina("A","Z")
    # print (recorrido)

if __name__ == "__main__":
    main()
    
