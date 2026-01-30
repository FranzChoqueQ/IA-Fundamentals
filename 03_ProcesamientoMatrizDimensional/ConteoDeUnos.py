matrix = [[1,0,1,0], 
          [0,1,0,1], 
          [0,1,0,1], 
          [0,0,0,0]]

def sum_ones(matrix):
    sum = 0
    for row in matrix:
        for element in row:
            if element == 1:
                sum += 1
                print(sum)
    return sum

total_ones = sum_ones(matrix)
print("La longitud total del rio es: ", total_ones)

