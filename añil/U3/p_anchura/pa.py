import json


def pa(inicio,fin):
    """
    algoritmo primero anchura 
    """
    #loading tree
    f = open('tree.json','r')
    tree = json.load(f)
    f.close()
    tree = tree["branches"]
    # print(tree)
    
    position = inicio
    recorrido = []
    recorrido += [position]
    buffer = []
    x = 0

    while 1:
        hijos = tree[position]["children"]
        if hijos:
            buffer+=hijos
        try:
            position = buffer[x]
        except:
           break 
        x+=1

    for element in buffer:
        recorrido += [element]
        if element == fin:
            break

    return recorrido 



    
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
    
    evaluation()
    # recorrido = pa("Z","ZZY")
    # print(recorrido)

if __name__ == "__main__":
    main()
 
