
from numpy.random import rand,randint
import random
# Create an initial population of random solutions
def initialize_GA(pop_size, num_variables, bounds):
    pop = []
    for _ in range(pop_size):
        solution = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(num_variables)]
        pop.append(solution)
    return pop