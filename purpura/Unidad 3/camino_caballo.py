from ruamel.yaml import YAML
import os, random

yaml=YAML()
yaml.default_flow_style =False
yaml.indent(sequence=4, offset=2)

def movimientoCaballo(x,y,c_x,c_y,n,m):
    x = x+c_x
    y = y+c_y
    if x >= 0 and x < n and y >= 0 and y < m:
        return x*8 + y

def generarAdyacencias(n,m,x,y):
    ady = []
    sumas = [[2,1],[1,2]]
    for i in [1,-1]:
        for j in sumas:
            ady.append(movimientoCaballo(x,y,j[0]*i,j[1]*i,n,m))
            ady.append(movimientoCaballo(x,y,j[0]*i,j[1]*(-i),n,m))
    return [x for x in ady if x != None]

def generarMatriz(n,m):
    mat = []
    for x in range(n):
        for y in range(m):
            aristas = [0 for i in range(n*m)]
            adyacencias = generarAdyacencias(n,m,x,y)
            for i in adyacencias:
                aristas[i] = 1
            mat.append(aristas)
    return mat

if os.path.isfile("matriz.yaml"):
    s=open("matriz.yaml","r")
    Data = yaml.load(s)
    s.close() 
    mat = Data["matriz"]
else:
    mat = generarMatriz(8,8)
    r = open("matriz.yaml","w")
    yaml.dump({'matriz':mat},r)
    r.close()
n = len(mat)

def obtenerGrado(nodo,stack):
    cont = 0
    for i in range(len(nodo)):
        if nodo[i] and not (i in stack):
            cont+=1
    return cont

def siguienteNodo(adj,v,stack):
    minimo = 8
    indice_minimo = -1
    inicio = random.randint(0, 1000) % len(adj)
    for i in range(len(adj[v])):
        j = (i + inicio) % 64
        if adj[v][j] and not (j in stack):
            grado = obtenerGrado(adj[j],stack)
            if grado < minimo:
                minimo = grado
                indice_minimo = j
    if indice_minimo == -1:
        return None
    else:
        return indice_minimo

def encontrarCamino(v,adj,stack):
    if v == None:
        return stack
    stack = stack + [v]
    return encontrarCamino(siguienteNodo(adj,v,stack),adj,stack)


def main():
    num = int(input("Considerando el tablero anterior, elija el número de casilla donde iniciará el camino: "))
    stack = encontrarCamino(num,mat,[])
    while not len(stack) == 64:
        stack = encontrarCamino(num,mat,[])
        #print((stack))
    for i in (convTablero(stack)):
        print(i)

def generarMatCu(n,c):
    matriz = []
    for i in range(n):
        matriz.append([c]*n)     
    return matriz      

def imprimirTablero():
    tablero = generarMatCu(8,"")
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            tablero[i][j] = 7-i + (8*j)
        print(tablero[i])

def convTablero(stack):
    tablero = generarMatCu(8,"")
    for i in range(len(stack)):
        tablero[7 - stack[i]%8][stack[i]//8] = i + 1
    return tablero

imprimirTablero()
main()