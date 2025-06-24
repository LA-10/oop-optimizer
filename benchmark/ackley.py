import numpy as np
import math 

def ackley(solution):
    a = 20.00
    b = 0.2
    c = 2 * math.pi

    solution = np.array(solution)

    term1 = -a * math.exp(-b * math.sqrt(np.mean(solution**2)))
    term2 = -math.exp(np.mean(np.cos(c * solution)))

    return  term1 + term2 + a + math.exp(1)
