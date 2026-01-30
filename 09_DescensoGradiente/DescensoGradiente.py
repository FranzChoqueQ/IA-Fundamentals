#Decenso de gradiente

def square(x):
    return x*x

def gradient_descent(learning_rate, initial_guess, iterations):
    x = initial_guess
    for i in range(iterations):
        derivate = 2 * x
        x -= learning_rate * derivate
    return x

learning_rate = 0.1
initial_guess = 2

minimum_value = gradient_descent(learning_rate, initial_guess,100)
print("Minimum value found:", minimum_value)

