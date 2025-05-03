class ComeSolo:
    def __init__(self):
        # Definimos el tablero como una lista de listas
        self.tablero = [
            [1],           # A
            [1, 1],       # B
            [1, 1, 1],    # C
            [1, 1, 1, 1], # D
            [1, 1, 1, 1, 1] # E
        ]
        self.direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1)]  # Movimientos posibles
        self.movimientos = []  # Lista para guardar los movimientos realizados

    def imprimir_tablero(self):
        # Imprimir el tablero con formato específico
        for i, fila in enumerate(self.tablero):
            print(" " * (5 - i) + " ".join(str(x) if x == 1 else '0' for x in fila))
        print()  # Nueva línea para separar visualmente

    def mover(self, x, y, dx, dy):
        """Realiza un movimiento saltando una pieza."""
        self.tablero[x + dx][y + dy] = 0  # Eliminar la pieza saltada
        self.tablero[x][y] = 0  # Eliminar la pieza que se mueve
        self.tablero[x + 2 * dx][y + 2 * dy] = 1  # Colocar la pieza en la nueva posición
        # Agregar movimiento a la lista en orden correcto
        self.movimientos.append((x, y, x + 2 * dx, y + 2 * dy))  # Guardar el movimiento

    def deshacer_movimiento(self, x, y, dx, dy):
        """Deshace un movimiento."""
        self.tablero[x + dx][y + dy] = 1  # Recuperar la pieza saltada
        self.tablero[x][y] = 1  # Recuperar la pieza que se mueve
        self.tablero[x + 2 * dx][y + 2 * dy] = 0  # Eliminar la pieza en la nueva posición
        # Eliminar el movimiento del historial
        self.movimientos.pop()

    def es_movimiento_valido(self, x, y, dx, dy):
        """Verifica si un movimiento es válido."""
        if (0 <= x + 2 * dx < len(self.tablero) and 
            0 <= y + 2 * dy < len(self.tablero[x + 2 * dx]) and 
            self.tablero[x + dx][y + dy] == 1 and 
            self.tablero[x + 2 * dx][y + 2 * dy] == 0):
            return True
        return False

    def resolver(self, piezas_restantes):
        """Resuelve el juego buscando una solución."""
        if piezas_restantes == 1:
            return True  # Solo queda una pieza

        for x in range(len(self.tablero)):
            for y in range(len(self.tablero[x])):
                if self.tablero[x][y] == 1:  # Si hay una pieza en la posición
                    for dx, dy in self.direcciones:
                        if self.es_movimiento_valido(x, y, dx, dy):
                            # Guardamos la posición inicial
                            x_inicial, y_inicial = x, y
                            self.mover(x, y, dx, dy)  # Realizar el movimiento
                            
                            # Imprimir el movimiento realizado
                            print(f"Movido de ({chr(y + 2 * dy + ord('A'))}{x + 2 * dx + 1}) a ({chr(y_inicial + ord('A'))}{x_inicial + 1})")
                            self.imprimir_tablero()  # Imprimir tablero después del movimiento
                            
                            if self.resolver(piezas_restantes - 1):
                                return True  # Si se encontró solución
                            
                            self.deshacer_movimiento(x, y, dx, dy)  # Deshacer el movimiento
        return False  # No se encontró solución

def main():
    juego = ComeSolo()
    
    # Solicitar la posición libre al usuario
    print("Tablero inicial (con piezas):")
    juego.imprimir_tablero()
    
    # Entradas de coordenadas para la posición vacía (debe ser dentro del rango)
    pos_libre = input("Introduce la posición vacía (ej. 'C3'): ").strip().upper()
    
    # Conversión de coordenadas
    fila = ord(pos_libre[0]) - ord('A')  # Convertir letra a índice de fila
    columna = int(pos_libre[1]) - 1  # Convertir número a índice de columna

    # Verificar que la posición es válida
    if fila < 0 or fila >= len(juego.tablero) or columna < 0 or columna >= len(juego.tablero[fila]):
        print("Posición inválida.")
        return

    # Establecer la posición vacía
    juego.tablero[fila][columna] = 0  # Establecer la posición vacía
    print("\nTablero después de establecer la posición vacía:")
    juego.imprimir_tablero()

    # Contar las piezas restantes
    piezas_restantes = sum(sum(fila) for fila in juego.tablero)
    
    # Intentar resolver el juego
    if juego.resolver(piezas_restantes):
        print("\n¡Se encontró una solución!")
        print("Movimientos realizados:")
        for (x_inicial, y_inicial, x_final, y_final) in juego.movimientos:
            print(f"Movido de ({chr(y_inicial + ord('A'))}{x_inicial + 1}) a ({chr(y_final + ord('A'))}{x_final + 1})")
    else:
        print("\nNo se encontró solución.")

if __name__ == "__main__":
    main()