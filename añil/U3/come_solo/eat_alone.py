def print_board(board):
    n = len(board)
    for i in range(n):
        print(' ' * (n - i - 1), end='')
        for j in range(i + 1):
            print('O ' if board[i][j] else '. ', end='')
        print()

def count_pegs(board):
    return sum(sum(row) for row in board)

def is_valid_move(board, from_row, from_col, to_row, to_col):
    if not (0 <= from_row < len(board) and 0 <= from_col <= from_row):
        return False
    if not (0 <= to_row < len(board) and 0 <= to_col <= to_row):
        return False
    if not board[from_row][from_col] or board[to_row][to_col]:
        return False
    
    dr = to_row - from_row
    dc = to_col - from_col
    
    # Direcciones permitidas
    if (dr, dc) not in [(0, 2), (0, -2), (2, 0), (-2, 0), (2, 2), (-2, -2)]:
        return False
    
    mid_row, mid_col = from_row + dr//2, from_col + dc//2
    
    if not (0 <= mid_row < len(board) and 0 <= mid_col <= mid_row):
        return False
    
    return board[mid_row][mid_col]

def make_move(board, from_row, from_col, to_row, to_col):
    new_board = [row.copy() for row in board]
    dr = to_row - from_row
    dc = to_col - from_col
    mid_row = from_row + dr//2
    mid_col = from_col + dc//2
    
    new_board[from_row][from_col] = False
    new_board[mid_row][mid_col] = False
    new_board[to_row][to_col] = True
    return new_board

def solve(board, visited, path):
    if count_pegs(board) == 1:
        return path
    
    state = tuple(tuple(row) for row in board)
    if state in visited:
        return None
    visited.add(state)
    
    # Generar todos los movimientos posibles
    for i in range(len(board)):
        for j in range(i + 1):
            if board[i][j]:
                # Intentar todas las direcciones posibles
                directions = [
                    (0, 2), (0, -2),  # Horizontal
                    (2, 0), (-2, 0),  # Vertical
                    (2, 2), (-2, -2)  # Diagonal
                ]
                for dr, dc in directions:
                    to_i = i + dr
                    to_j = j + dc
                    if is_valid_move(board, i, j, to_i, to_j):
                        new_board = make_move(board, i, j, to_i, to_j)
                        result = solve(new_board, visited.copy(), path + [(i, j, to_i, to_j)])
                        if result:
                            return result
    return None

def main():
    size = 5
    board = [[True for _ in range(i+1)] for i in range(size)]
    
    print("¡Bienvenido al ComeSolo Autosolver!")
    print_board(board)
    
    # Eliminar primera pieza
    while True:
        try:
            fr, fc = map(int, input("\nElige la posición inicial vacía (fila columna): ").split())
            if 0 <= fr < size and 0 <= fc <= fr and board[fr][fc]:
                board[fr][fc] = False
                break
            else:
                print("Posición inválida")
        except:
            print("Entrada inválida")
    
    # Resolver automáticamente
    print("\nResolviendo...")
    visited = set()
    solution = solve(board, visited, [])
    
    if solution:
        print("\nSolución encontrada!")
        step = 1
        current_board = board
        for move in solution:
            print(f"\nPaso {step}:")
            from_row, from_col, to_row, to_col = move
            current_board = make_move(current_board, from_row, from_col, to_row, to_col)
            print_board(current_board)
            step += 1
    else:
        print("\nNo se encontró solución para esta configuración inicial")

if __name__ == "__main__":
    main()
