
def imprimir_tablero(grid):
    print(" - - - - - - -")
    for fila in grid:
        print("|  " + "  ".join(str(value) if isinstance(value, str) else "." for value in fila))
    print()


def available_squares_calc(grid,x,y):

    if grid[x][y] !=0:
        return False

    length_row = len(grid[x]) 
    length_column = len(grid) 


    #verify positions x 

    for i in range(x):
        if grid[i][y] != 0 :
            return False 
    for i in range(x+1,length_column):
        if grid[i][y] != 0:
            return False

    #verify positions y 
    for i in range(y):
        if grid[x][i] != 0:
            return False
    for i in range(y+1,length_row):
        if grid[x][i] != 0: 
            return False

    #verify diagonals 
    a = x+1
    b = y+1

    while a < length_column and b < length_row :
        if grid[a][b] != 0:
            return False
        else:
            a+=1
            b+=1

    a = x-1
    b = y-1

    while a >= 0 and b >= 0:
        if grid[a][b] != 0:
            return False
        else:
            a-=1
            b-=1

    a = x-1
    b = y+1

    while a >=0 and b < length_row:
        if grid[a][b] != 0:
            return False
        else:
            a-=1
            b+=1

    a = x+1
    b = y-1

    while a < length_column and b >= 0:
        if grid[a][b] != 0:
            return False
        else:
            a+=1
            b-=1

    return grid 


def queen_bruteforce(grid,x,y, queen_counter=None):
    if queen_counter == 0:
        return [grid]
    elif queen_counter == None:
        queen_counter = 4

    if grid[x][y] != 0:
        return []

    grid_copy = [element[:] for element in grid]
    resp = available_squares_calc(grid_copy,x,y)
    if resp != False:
        grid = [element[:] for element in resp] 
        grid[x][y] = "♕"
        # imprimir_tablero(grid)
        queen_counter -=1
        grid_copy = [element[:] for element in grid]
        result = []
        for i in range (len(grid_copy)):
            for j in range (len(grid_copy[i])):
                result += queen_bruteforce(grid_copy,i,j,queen_counter) 
        return result
    else:
        return []


grid = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

solution=[]

for x in range(len(grid)):
    for y in range(len(grid[x])):
        # solution=queen_bruteforce(grid,x,y)
        grid_copy = [element[:] for element in grid]
        solution += queen_bruteforce(grid_copy,x,y)

# Filtra duplicados (opcional)
unique_solutions = []
for sol in solution:
    if all(sol != u for u in unique_solutions):
        unique_solutions.append(sol)

# Muestra soluciones
for resp in unique_solutions:
    imprimir_tablero(resp)
