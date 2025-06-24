import math 

def rastrigin(solution, A = 10):
    n = len(solution)

    sum = 0.0

    for i in range(n):
        sum += (solution[i] ** 2 - A * math.cos(2 * math.pi * solution[i]))

    return A * n + sum