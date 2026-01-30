import random
import matplotlib.pyplot as plt

def generate_maze(rows, cols):
    # Crear laberinto lleno de paredes (1)
    maze = [[1 for _ in range(cols)] for _ in range(rows)]

    def dfs(row, col):
        directions = [(0,1), (0,-1), (1,0), (-1,0)]  # Derecha, Izquierda, Abajo, Arriba
        random.shuffle(directions)

        for dr, dc in directions:
            r, c = row + 2 * dr, col + 2 * dc
            if 0 <= r < rows and 0 <= c < cols and maze[r][c] == 1:
                maze[row + dr][col + dc] = 0  # Abrir camino intermedio
                maze[r][c] = 0  # Abrir celda destino
                dfs(r, c)

    # Seleccionar un punto de inicio aleatorio en una celda par
    start_row, start_col = random.randrange(0, rows, 2), random.randrange(0, cols, 2)
    maze[start_row][start_col] = 0  # Abrir inicio
    dfs(start_row, start_col)

    return maze

def plot_maze(maze):
    plt.figure(figsize=(10,5))
    plt.imshow(maze, cmap=plt.cm.binary, interpolation='nearest')
    plt.xticks([]) 
    plt.yticks([])
    plt.show()   # O tambien █ 

# Parámetros del laberinto
rows, cols = 21,42
maze = generate_maze(rows, cols)
plot_maze(maze)
