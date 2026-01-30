matriz = [[0,1,1,1,1,0,0,0,0,0], 
          [0,0,0,0,0,0,0,0,1,0], 
          [1,0,1,0,0,0,0,0,1,0], 
          [1,0,1,0,0,1,0,0,1,0],
          [1,0,0,0,0,0,0,0,0,0],
          [1,0,1,1,1,1,1,1,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,1,1,1,0,0,0,0,0,0]]

def contar_rio(matriz):
    if not matriz:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    visitado = [[False] * columnas for _ in range(filas)]
    longitudes = []

    def dfs(i, j):
        """Busca en profundidad todas las celdas conectadas (DFS)"""
        stack = [(i, j)]
        tamaño = 0

        while stack:
            x, y = stack.pop()
            if visitado[x][y]:
                continue
            visitado[x][y] = True
            tamaño += 1

            # Direcciones: arriba, abajo, izquierda, derecha
            direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in direcciones:
                nx, ny = x + dx, y + dy
                if 0 <= nx < filas and 0 <= ny < columnas and matriz[nx][ny] == 1 and not visitado[nx][ny]:
                    stack.append((nx, ny))

        return tamaño

    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == 1 and not visitado[i][j]:
                longitudes.append(dfs(i, j))

    return longitudes

print(contar_rio(matriz))
