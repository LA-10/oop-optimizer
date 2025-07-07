import random

def bar():
    print('-' * 20)


def evaluate_fitness(solution, func):
    # Sphere funct
    return func(solution)



def create_parent(population_vector, func):
    fitness = [evaluate_fitness(solution, func) for solution in population_vector]

    best_index = fitness.index(min(fitness))

    return population_vector[best_index], best_index

                

def create_child(parent_solution, status_solution, D,  lb, ub):
    child_solution = []
    for i in range(D):
        if status_solution[i] == 0 or status_solution[i] == 1:
            child_solution.append(parent_solution[i])
        else:
            child_solution.append(random.uniform(lb, ub))

    return child_solution     


        
# applied at the end of each iteration
def mutation(status_solution, MR, D):
    for i in range(D):
        if random.uniform(0,1) < MR:
            status_solution[i] = random.randint(0, 2)

    return status_solution
