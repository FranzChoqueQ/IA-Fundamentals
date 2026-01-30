import random

MAZE = [
    [0,0,1,0,0],
    [1,0,1,0,1],
    [0,0,0,0,0],
    [0,1,1,1,1],
    [0,0,0,0,0]
]
START = (0,0)
GOAL = (4,4)

DIRECTIONS = [(0,1), (1,0),(0,-1),(-1,0)]

def is_valid_move(position):
    x,y = position
    return 0<=x<len(MAZE) and 0<=y<len(MAZE[0]) and MAZE[x][y] == 0

class Individual:
    def __init__(self,genes=None, max_steps=20):
        if genes is None:
            self.genes = [random.choice(DIRECTIONS) for _ in range(max_steps)]
        else:
            self.genes = genes

        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        position = START
        steps = 0
        for direction in self.genes:
            new_position = (position[0]+direction[0],position[1]+direction[1])
            if is_valid_move(new_position):
                position = new_position
                steps += 1
                if position == GOAL:
                    return 1000-steps    
            else:
                break

        distance_to_goal = abs(position[0]-GOAL[0])+abs(position[1]-GOAL[1])
        return -distance_to_goal
    
def selection(population):
    population.sort(key=lambda ind: ind.fitness, reverse = True)
    return population[:len(population)//2]

def crossover(parent1,parent2):
    crossover_point = random.randint(1, len(parent1.genes)-1)
    child_genes = parent1.genes[:crossover_point]+parent2.genes[crossover_point:]
    return Individual(child_genes)

def mutation(individual):
    if random.random()<0.1:
        index = random.randint(0,len(individual.genes)-1)
        individual.genes[index] = random.choice(DIRECTIONS)
    return individual
    

def generic_algorithm(population_size, generations, max_steps = 20):
    population = [Individual(max_steps=max_steps) for _ in range(population_size)]
    for generation in range(generations):
        selected = selection(population)
        next_generation = []
        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(selected,2)
            child = crossover(parent1, parent2)
            next_generation.append(mutation(child))
            population = next_generation
            best_individual = max(population, key=lambda ind:ind.fitness)
            print(f"Generation {generation}: Best fitness = {best_individual.fitness}")
            if best_individual.fitness >= 1000:
                print(f"Goal reached in generation {generation}")
                break

            return best_individual

def print_path(individual):
    position = START
    path = [position]
    for direction in individual.genes:
        new_position = (position[0]+direction[0],position[1]+direction[1])
        if is_valid_move(new_position):
            position = new_position
            path.append(position)
            if position ==GOAL:
                break
        else:
            break
        return path
    
if __name__ == "__main__":
    best_path = generic_algorithm(population_size=100, generations=50, max_steps=20)
    print(f"Best path genes:", best_path.genes)
    path_positions = print_path(best_path)
    print("Best path positions: ", path_positions)
        


