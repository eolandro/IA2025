import json

def pp(inicio,fin,tree=None,position=None,recorrido=None,buffer=None):
    """
    algoritmo primero profundidad 
    """
       

    if (tree is None):        
        position = inicio
        recorrido = []
        buffer = []

        #loading tree
        f = open('tree.json','r')
        tree = json.load(f)
        f.close()
        tree = tree["branches"]
    

    recorrido += [position] 
    # print(recorrido) 

    if position == fin:
        return recorrido
    hijos = tree[position]["children"]
    if hijos:
        position = hijos.pop(0)

        buffer = buffer + [hijo for hijo in hijos[::-1]]
        return pp(inicio,fin,tree,position,recorrido,buffer)
    else:
        position = buffer.pop()
        return pp(inicio,fin,tree,position,recorrido,buffer)
        
        
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

    f = open('tree.json','r')
    tree = json.load(f)
    f.close()
    tree = tree["branches"]
    print("\n--- Algoritmo primero profundidad ---")
    print(" formato: pp(inicio,fin)\n")
    
    evaluation()
    # recorrido = pp("Z","ZX")
    # print (recorrido)

if __name__ == "__main__":
    main()
 
