import numpy as np

def griewank(solution): 

    solution = np.array(solution)

    sum_term = np.sum(solution**2 / 4000)
    product_term = np.prod(np.cos(solution / np.sqrt(np.arange(1, len(solution) + 1))))

    return sum_term - product_term + 1