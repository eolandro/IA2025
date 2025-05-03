class Nodo:
    def __init__(self, tab, mov=None, padre=None):
        self.tab = tab
        self.mov = mov
        self.padre = padre
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)


class JuegoPeg:
    def __init__(self, vacio):
        self.tab = [[1] * (i + 1) for i in range(5)]
        self.tab[vacio[0]][vacio[1]] = 0
        self.raiz = Nodo(self.tab)
        self.meta = None
        self.visit = set()

    def gen_movs(self, nodo):
        dirs = [(0, 2), (0, -2), (2, 0), (-2, 0), (2, 2), (-2, -2)]
        t, movs = nodo.tab, []
        for i in range(len(t)):
            for j in range(len(t[i])):
                if t[i][j] == 1:
                    for dx, dy in dirs:
                        x2, y2 = i + dx, j + dy
                        xm, ym = i + dx // 2, j + dy // 2
                        if 0 <= x2 < len(t) and 0 <= y2 < len(t[x2]) and t[x2][y2] == 0 and t[xm][ym] == 1:
                            nuev_tab = [fila[:] for fila in t]
                            nuev_tab[i][j] = 0
                            nuev_tab[xm][ym] = 0
                            nuev_tab[x2][y2] = 1
                            movs.append((nuev_tab, (i, j, x2, y2)))
        return movs

    def gen_arbol(self):
        nivel = [self.raiz]
        self.visit.add(str(self.raiz.tab))

        while nivel:
            sig = []
            for nodo in nivel:
                for nuev_tab, mov in self.gen_movs(nodo):
                    clave = str(nuev_tab)
                    if clave not in self.visit:
                        nuevo = Nodo(nuev_tab, mov, nodo)
                        nodo.agregar_hijo(nuevo)
                        sig.append(nuevo)
                        self.visit.add(clave)
                        if self.es_meta(nuev_tab):
                            self.meta = nuevo
                            return
            nivel = sig

    def es_meta(self, tab):
        return sum(f.count(1) for f in tab) == 1

    def impr_sol(self):
        if not self.meta:
            print('No se encontró solución')
            return

        camino, nodo = [], self.meta
        while nodo:
            camino.append((nodo.tab, nodo.mov))
            nodo = nodo.padre

        for i, (tab, mov) in enumerate(reversed(camino[:-1]), 1):
            print(f'\nMovimiento {i}: {mov[:2]} a {mov[2:]}')
            self.impr_tab(tab)

    def impr_tab(self, tab):
        for i, fila in enumerate(tab):
            print(' ' * (4 - i) + ' '.join('0' if c == 1 else '_' for c in fila))


def impr_coords(n):
    for i in range(n):
        print('   ' * (n - i - 1), end='')
        for j in range(i + 1):
            print(f'{i},{j}', end='   ')
        print()


def main():
    print("\n=========== ¡¡¡ BIENVENIDO AL JUEGO COME SOLO !!! ===========\n")
    print("Coordenadas disponibles:\n")
    impr_coords(5)
    entrada = input('\nElige una posición vacía (fila,col): ')
    vacio = tuple(map(int, entrada.strip('()').split(',')))

    juego = JuegoPeg(vacio)
    print("\nEstado inicial del tablero:")
    juego.impr_tab(juego.tab)
    juego.gen_arbol()
    print("\n=========== SOLUCIÓN ===========")
    juego.impr_sol()


if __name__ == '__main__':
    main()
