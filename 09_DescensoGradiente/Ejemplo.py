import numpy as np

# — Parte 1: Conversión de array a float —  
initial_position = np.array([1, 2, 3, 4])  
position = initial_position.astype(float)  
print("Original array (initial_position):", initial_position)  
print("Converted array (position):", position)  

# — Parte 2: Distancia Euclidiana Negativa —  
position = np.array([1, 1])  
goal = np.array([4, 5])  
negative_distance = -np.linalg.norm(position - goal)  
print("Negative Euclidean Distance:", negative_distance)  

# — Parte 3: Descenso del Gradiente para Planificación de Movimiento del Robot —

# Función de costo  
def cost_function(position, goal):  
    return -np.linalg.norm(position - goal)  

# Gradiente de la función de costo  
def gradient(position, goal):  
    return -(position - goal) / np.linalg.norm(position - goal)  

# Algoritmo de descenso del gradiente  
def gradient_descent(learning_rate, initial_position, goal, obstacles, iterations):  
    position = initial_position.astype(float)  
    goal = goal.astype(float)  
    obstacles = [obstacle.astype(float) for obstacle in obstacles]  
    repulsion_strength = 0.5 # Controla la fuerza de repulsión de obstáculos  
    
    for i in range(iterations):  
        grad = gradient(position, goal)  
        for obstacle in obstacles:  
            distance = np.linalg.norm(position - obstacle)  
            if distance < 1.0:  
                grad += repulsion_strength * (position - obstacle) / distance  
        position += learning_rate * grad  
    return position  

# Parámetros  
learning_rate = 0.1  
initial_position = np.array([0, 0])  
goal = np.array([5, 5])  
obstacles = [np.array([2, 2]), np.array([3, 3])]  
iterations = 100  

# Ejecutar el algoritmo  
final_position = gradient_descent(learning_rate, initial_position, goal, obstacles, iterations)  
print("Final Position:", final_position)