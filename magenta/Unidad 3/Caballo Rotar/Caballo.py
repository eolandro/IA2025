def rotar(mat, r, resu):
    resu.append([fila[:] for fila in mat])
    if r == 0:
        return resu

    n = len(mat)
   
    borde = mat[0][:] + [mat[i][n-1] for i in range(1, n-1)] + mat[n-1][::-1] + [mat[i][0] for i in range(n-2, 0, -1)]

 
    borde = borde[-3:] + borde[:-3]

    idx = 0
    for j in range(n):  # fila superior
        mat[0][j] = borde[idx]; idx += 1
    for i in range(1, n-1):  # columna derecha
        mat[i][n-1] = borde[idx]; idx += 1
    for j in range(n-1, -1, -1):  # fila inferior
        mat[n-1][j] = borde[idx]; idx += 1
    for i in range(n-2, 0, -1):  # columna izquierda
        mat[i][0] = borde[idx]; idx += 1

    return rotar(mat, r - 1, resu)

# Prueba
mat = [['_'] * 3 for _ in range(3)]
mat[0][0] = 'R'
mat[0][2] = 'R'
mat[2][0] = 'A'
mat[2][2] = 'A'
rota = 4

resul = rotar(mat, rota, [])
for s, matriz in enumerate(resul):
    print(f"Rotación {s}:")
    for fila in matriz:
        print(fila)
    print()
