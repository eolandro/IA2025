def generarTableroInicial(inicio):
    tablero = []
    cont = 0
    for i in range(5):
        tablero.append([])
        for j in range(i+1):
            if inicio == cont:
                tablero[i].append(0)
            else:
                tablero[i].append(1)
            cont += 1
    return tablero

def generarListaInicial(inicio):
    lista = [1]*15
    lista[inicio] = 0
    return lista

def generarTableroEleccion():
    tablero = []
    cont = 0
    for i in range(5):
        tablero.append([])
        for j in range(i+1):
            tablero[i].append(cont)
            cont+=1
    return tablero

def generarTableroLista(lista):
    tablero = []
    cont = 0
    for i in range(5):
        tablero.append([])
        for j in range(i+1):
            tablero[i].append(lista[cont])
            cont+=1
    return tablero

matriz = [[(2,4),(3,6)],[(4,7),(5,9)],[(5,8),(6,10)],[(2,1),(5,6),(7,11),(8,13)]
          ,[(8,12),(9,14)],[(3,1),(5,4),(9,13),(10,15)],[(4,2),(8,9)]
          ,[(5,3),(9,10)],[(5,2),(8,7)],[(6,3),(9,8)],[(7,4),(12,13)]
          ,[(8,5),(13,14)],[(8,4),(9,6),(12,11),(14,15)],[(9,5),(13,12)]
          ,[(10,6),(14,13)]]

def imprimirTablero(tablero):
    for i in (tablero):
        print("{:^22}".format(str(i)))

def camino(mat,origen):
    lisTab = generarListaInicial(origen)
    solucion = recursiva(lisTab,mat,[0]*13,0)
    return solucion

def recursiva(lista,mat,pila,cont):
    if sum(lista) == 1:
        return pila
    movs = generarMovs(lista.copy(),mat)
    for i in movs:
        pila[cont] = (i[0],i[2])
        camino = recursiva(modTablero(lista.copy(),i),mat,pila,cont+1)
        if camino:
            return camino
    return False
        

def generarMovs(lista,mat):
    movimientos = []
    #movs = generarMovs(lisTab,mat)
    for i in range(len(lista)):
        for j in mat[i]:
            if lista[i] and lista[j[0]-1] and not lista[j[1]-1]:
                movimientos.append((i,j[0]-1,j[1]-1))
    return movimientos

def modTablero(lista,movimiento):
    lista[movimiento[0]] = 0
    lista[movimiento[1]] = 0
    lista[movimiento[2]] = 1
    return lista


imprimirTablero(generarTableroEleccion())
inicio = int(input("Escriba el nodo donde iniciar: "))
print("Solución: ")

print(camino(matriz,inicio))


