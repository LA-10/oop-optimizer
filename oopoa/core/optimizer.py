import numpy as np
import random
from .population import *
    


def optimizer_code(Max_Iter, N, D, lb, ub, MR, func):

    inital_pop = [[random.uniform(lb, ub) for x in range(D)] for y in range(N)]
    inital_status = [[random.randint(0, 2) for x in range(D)] for y in range(N)]

    # Creating population vector
    population = np.array(inital_pop)

    # Creating status vector
    #   0 -> public
    #   1 -> protected
    #   2 -> private
    status = np.array(inital_status)

    #  Main Optimization Loop 
    best_fitness = []

    for i in range(Max_Iter):
        parent_solution, best_index = create_parent(population, func)
        child_solution = create_child(parent_solution, status[best_index], D, lb, ub)

        parent_fitness = evaluate_fitness(parent_solution, func)
        child_fitness = evaluate_fitness(child_solution, func)


        if child_fitness < parent_fitness:

            population[best_index] = child_solution
        
        fitnesses = [evaluate_fitness(sol, func) for sol in population]
        best_fitness.append(min(fitnesses))

        status[best_index] = mutation(status[best_index], MR, D)

    return best_fitness
