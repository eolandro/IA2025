def imprimir_tablero(grid):
    print(" - - - - - - -")
    for fila in grid:
        print("|  " + "  ".join(str(value) if isinstance(value, str) else "." for value in fila))
    print()



def posible_move(grid,x,y,move):
    return 0 <= x + move[0] < len(grid) and 0 <= y + move[1] < len(grid[0])
    
 

def rotar_caballos(grid,n):
    resultados =[]
    # knight_moves = [[1,2],[2,-1],[-1,-2],[-2,1],[2,1],[1,-2],[-2,-1],[-1,2]]
    
    knight_moves = [
        [-2, -1],  
        [-1, -2], 
        [1, -2],  
        [2, -1],  
        [2, 1],  
        [1, 2],    
        [-1, 2],   
        [-2, 1],   
    ]

    current_grid = [element[:] for element in grid]

    for rotacion_n in range(n):
        piece_positions = []

        #find pieces
        for x,row in enumerate(current_grid):
            for y,element in enumerate(row):
                if current_grid[x][y] != 0:
                    piece_positions+=[[x,y]]
                    
        #reorganizar posiciones
        half = len(piece_positions) // 2 
        piece_positions = piece_positions[:half] + piece_positions[half:][::-1]

        new_grid = [[0 for _ in row] for row in current_grid]

        #rotacion de 4 piezas si es posible
        for position in piece_positions:
            x,y = position

            piece = current_grid[x][y]
            grid[x][y] = 0

            while 1:
                move = knight_moves[0]
                knight_moves = knight_moves[1:]+[move]
                new_x = x +move[0]
                new_y = y +move[1]

                # if posible_move(current_grid,x,y,move) and new_grid[new_x][new_y] == 0:
                if posible_move(current_grid,x,y,move) :
                    new_grid[new_x][new_y] = piece
                    break

        current_grid = [element[:] for element in new_grid]
        resultados.append(current_grid)
    return resultados

grid = [
    ["♘",0,"♘"],
    [0,0,0],
    ["♞",0,"♞"]
]

solution=[]

# grid_copy = [element[:] for element in grid]

resultados = rotar_caballos([element[:] for element in grid],4)

imprimir_tablero(grid) 
for posicion in resultados:
    imprimir_tablero(posicion)


