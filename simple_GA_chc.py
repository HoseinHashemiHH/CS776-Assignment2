


from chc_GA import chc_selection
import math
from objective_functions import f1,f2,f3,f4,f5
import numpy as np
from numpy.random import rand,randint
import random
from selection import selection
from flip import mutate
from xover import five_parent_crossover
from init_GA import initialize_GA
from params import CHC_Params,Params_F1,Params_F2,Params_F3,Params_F4,Params_F5
from binary_float import binary_float

# Genetic algorithm
def genetic_algorithm(objective_func, num_variables, bounds, pop_size, num_generations, mutation_rate, mutation_scale):
    population = initialize_GA(pop_size, num_variables, bounds)
    best_solution = None
    best_score = float('inf')
    for generation in range(num_generations):
        scores = [objective_func(solution) for solution in population]
        fi_over_sig_fi=[s/sum(scores) for s in scores]
        # for i in fi_over_sig_fi:
        #     for j in i:
        #         element=binary_float(fi_over_sig_fi[i][j])
        all_pop_prob=[[binary_float(i) for i in s] for s in population]
        ith_pop=[solution for solution in population]
        for i,x in enumerate(all_pop_prob):
            print("The decoded chromosome is{}  and the probability of fi/sigma(fi) is:{}".format(x,fi_over_sig_fi[i]))
        # Find the best solution in the current population
        current_best_index = np.argmin(scores)
        current_best_score = scores[current_best_index]
        if current_best_score < best_score:
            best_solution = population[current_best_index]
            best_score = current_best_score
        
        # Create the next generation
        new_population = []
        for _ in range(pop_size):
            parents = [chc_selection(population,f5) for _ in range(5)]  # Select 5 parents
            child = five_parent_crossover(parents)
            child = mutate(child, mutation_rate, mutation_scale, bounds)
            new_population.append(child)
        population = new_population
    
    return best_solution, best_score

# Define the search space (bounds)
# Replace N with the desired number of variables

obj_func=f5
pobj=Params_F5()
bounds=pobj.bounds
pobj1=CHC_Params()
n_bits=pobj1.n_bits
n_iter=pobj1.n_iter
r_cross=pobj1.r_cross
r_mut=pobj1.r_mut
n_pop=pobj1.n_pop
vars_num=pobj.vars_num
# Run the genetic algorithm
best_solution, best_score = genetic_algorithm(obj_func,vars_num, bounds, n_pop, n_iter, r_mut, r_cross)

print('Best Solution:', best_solution)
print('Objective Value:', best_score)
