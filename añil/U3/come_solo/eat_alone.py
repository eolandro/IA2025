import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_for_key():
    input("\nPresiona Enter para continuar...")

def generate_numbered_board(size):
    board = []
    counter = 1
    for i in range(size):
        row = []
        for j in range(i + 1):
            row.append(str(counter).zfill(2))
            counter += 1
        board.append(row)
    return board

def print_initial_pyramid(numbered_board):
    size = len(numbered_board)
    max_width = 3
    
    for i in range(size):
        leading_spaces = (size - i - 1) * max_width
        print(' ' * leading_spaces, end='')
        print((' ' * (max_width)).join(numbered_board[i]))
    print()

def print_game_pyramid(board):
    size = len(board)
    for i in range(size):
        leading_spaces = (size - i - 1) * 2
        print(' ' * leading_spaces, end='')
        for j in range(i + 1):
            print('◉ ' if board[i][j] else '○ ', end='')
        print()
    print()

def create_position_map(size):
    position_map = {}
    counter = 1
    for i in range(size):
        for j in range(i + 1):
            position_map[counter] = (i, j)
            counter += 1
    return position_map

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
    
    if (dr, dc) not in [(0, 2), (0, -2), (2, 0), (-2, 0), (2, 2), (-2, -2)]:
        return False
    
    mid_row = from_row + dr//2
    mid_col = from_col + dc//2
    
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
    
    for i in range(len(board)):
        for j in range(i + 1):
            if board[i][j]:
                directions = [
                    (0, 2), (0, -2), (2, 0), (-2, 0),
                    (2, 2), (-2, -2)
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
    initial_board = [[True for _ in range(i+1)] for i in range(size)]
    numbered_board = generate_numbered_board(size)
    position_map = create_position_map(size)
    reverse_position_map = {v: k for k, v in position_map.items()}
    
    print("¡Bienvenido al ComeSolo Autosolver!")
    print("\nTablero inicial (selecciona posición vacía):")
    print_initial_pyramid(numbered_board)
    
    while True:
        try:
            pos = int(input("\nIngresa el número de la posición inicial vacía: "))
            if pos not in position_map:
                print("Número inválido")
                continue
                
            fr, fc = position_map[pos]
            if initial_board[fr][fc]:
                initial_board[fr][fc] = False
                break
            else:
                print("¡Esa posición ya está vacía!")
        except ValueError:
            print("Debes ingresar un número válido")
    
    print("\nResolviendo...")
    visited = set()
    solution = solve(initial_board, visited, [])
    
    if solution:
        current_board = [row.copy() for row in initial_board]
        step = 1
        
        clear_screen()
        print("Configuración inicial:")
        print_game_pyramid(current_board)
        wait_for_key()
        
        move_summary = []
        for move in solution:
            clear_screen()
            print(f"Movimiento #{step}")
            from_row, from_col, to_row, to_col = move
            current_board = make_move(current_board, from_row, from_col, to_row, to_col)
            print_game_pyramid(current_board)
            
            # Registrar movimiento
            from_num = reverse_position_map[(from_row, from_col)]
            to_num = reverse_position_map[(to_row, to_col)]
            move_summary.append(f"{from_num} --> {to_num}")
            
            step += 1
            wait_for_key()

        # Mostrar resumen de movimientos
        clear_screen()
        print("\nResumen de movimientos:")
        print("-----------------------")
        for idx, movimiento in enumerate(move_summary, 1):
            print(f"{idx}: {movimiento}")
        print()
        
    else:
        print("\nNo hay solución para esta configuración")

if __name__ == "__main__":
    main()
