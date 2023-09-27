




from ave_list import ave_list
import math
from objective_functions import f1,f2,f3,f4,f5
import numpy as np
from numpy.random import rand,randint
import random
from selection import selection
from flip import mutate
from xover import five_parent_crossover
from init_GA import initialize_GA
from params import Params_F1,Params_F2,Params_F3,Params_F4,Params_F5
from binary_float import binary_float
from list_list import list_list
import matplotlib.pyplot as plt

num_gen=[]
min_obj=[]
max_obj=[]
ave_obj=[]
min_fitness=[]
max_fitness=[]
ave_fitness=[]
# Genetic algorithm
def genetic_algorithm(objective_func, num_variables, bounds, pop_size, num_generations, mutation_rate, mutation_scale):
    population = initialize_GA(pop_size, num_variables, bounds)
    best_solution = None
    best_score = float('inf')

    for generation in range(num_generations):
        scores = [objective_func(solution) for solution in population]
        num_gen.append(generation)
        fi_over_sig_fi=[s/sum(scores) for s in scores]
        ave_fitness.append(sum(fi_over_sig_fi)/len(fi_over_sig_fi))
        min_fitness.append(min(fi_over_sig_fi))
        max_fitness.append(max(fi_over_sig_fi))
        min_obj.append(min(scores))
        max_obj.append(max(scores))
        ave_obj.append(sum(scores)/len(scores))
        # for i in fi_over_sig_fi:
        #     for j in i:
        #         element=binary_float(fi_over_sig_fi[i][j])
        # all_pop_prob=[[binary_float(i) for i in s] for s in population]
        # ith_pop=[solution for solution in population]
        # for i,x in enumerate(all_pop_prob):
        #     print("The decoded chromosome is{}  and the probability of fi/sigma(fi) is:{}".format(x,fi_over_sig_fi[i]))
        # Find the best solution in the current population
        current_best_index = np.argmin(scores)
        current_best_score = scores[current_best_index]
        if current_best_score < best_score:
            best_solution = population[current_best_index]
            best_score = current_best_score
        
        # Create the next generation
        new_population = []
        for _ in range(pop_size):
            parents = [selection(population,scores) for _ in range(5)]  # Select 5 parents
            child = five_parent_crossover(parents)
            child = mutate(child, mutation_rate, mutation_scale, bounds)
            new_population.append(child)
        population = new_population
    return best_solution, best_score, min_fitness,max_fitness,ave_fitness,\
            min_obj,max_obj,ave_obj,num_gen

# Define the search space (bounds)
# Replace N with the desired number of variables

obj_func=f5
pobj=Params_F5()
bounds=pobj.bounds
n_bits=pobj.n_bits
n_iter=pobj.n_iter
r_cross=pobj.r_cross
r_mut=pobj.r_mut
n_pop=pobj.n_pop
vars_num=pobj.vars_num

#one run
all_outputs_single=[]
output_single=genetic_algorithm(obj_func,vars_num, bounds, n_pop, n_iter, r_mut, r_cross)
for i in range(9):
    all_outputs_single.append(output_single[i])
print(" the best solution is {}, objective value is {}".format(all_outputs_single[0],all_outputs_single[1]))






from ave_list import ave_list
import math
from objective_functions import f1,f2,f3,f4,f5
import numpy as np
from numpy.random import rand,randint
import random
from selection import selection
from flip import mutate
from xover import five_parent_crossover
from init_GA import initialize_GA
from params import Params_F1,Params_F2,Params_F3,Params_F4,Params_F5
from binary_float import binary_float
from list_list import list_list
import matplotlib.pyplot as plt

num_gen=[]
min_obj=[]
max_obj=[]
ave_obj=[]
min_fitness=[]
max_fitness=[]
ave_fitness=[]
# Genetic algorithm
def genetic_algorithm(objective_func, num_variables, bounds, pop_size, num_generations, mutation_rate, mutation_scale):
    population = initialize_GA(pop_size, num_variables, bounds)
    best_solution = None
    best_score = float('inf')

    for generation in range(num_generations):
        scores = [objective_func(solution) for solution in population]
        num_gen.append(generation)
        fi_over_sig_fi=[s/sum(scores) for s in scores]
        ave_fitness.append(sum(fi_over_sig_fi)/len(fi_over_sig_fi))
        min_fitness.append(min(fi_over_sig_fi))
        max_fitness.append(max(fi_over_sig_fi))
        min_obj.append(min(scores))
        max_obj.append(max(scores))
        ave_obj.append(sum(scores)/len(scores))
        # for i in fi_over_sig_fi:
        #     for j in i:
        #         element=binary_float(fi_over_sig_fi[i][j])
        # all_pop_prob=[[binary_float(i) for i in s] for s in population]
        # ith_pop=[solution for solution in population]
        # for i,x in enumerate(all_pop_prob):
        #     print("The decoded chromosome is{}  and the probability of fi/sigma(fi) is:{}".format(x,fi_over_sig_fi[i]))
        # Find the best solution in the current population
        current_best_index = np.argmin(scores)
        current_best_score = scores[current_best_index]
        if current_best_score < best_score:
            best_solution = population[current_best_index]
            best_score = current_best_score
        
        # Create the next generation
        new_population = []
        for _ in range(pop_size):
            parents = [selection(population,scores) for _ in range(5)]  # Select 5 parents
            child = five_parent_crossover(parents)
            child = mutate(child, mutation_rate, mutation_scale, bounds)
            new_population.append(child)
        population = new_population
    return best_solution, best_score, min_fitness,max_fitness,ave_fitness,\
            min_obj,max_obj,ave_obj,num_gen

# Define the search space (bounds)
# Replace N with the desired number of variables

obj_func=f3
pobj=Params_F3()
bounds=pobj.bounds
n_bits=pobj.n_bits
n_iter=pobj.n_iter
r_cross=pobj.r_cross
r_mut=pobj.r_mut
n_pop=pobj.n_pop
vars_num=pobj.vars_num

#one run
all_outputs_single=[]
output_single=genetic_algorithm(obj_func,vars_num, bounds, n_pop, n_iter, r_mut, r_cross)
for i in range(9):
    all_outputs_single.append(output_single[i])
print(" the best solution is {}, objective value is {}".format(all_outputs_single[0],all_outputs_single[1]))


obj_func=f5
pobj=Params_F5()
bounds=pobj.bounds
n_bits=pobj.n_bits
n_iter=pobj.n_iter*2
r_cross=pobj.r_cross*2
r_mut=pobj.r_mut
n_pop=pobj.n_pop*5
vars_num=pobj.vars_num

#one run
all_outputs_single=[]
output_single=genetic_algorithm(obj_func,vars_num, bounds, n_pop, n_iter, r_mut, r_cross)
for i in range(9):
    all_outputs_single.append(output_single[i])
print(" the best solution is {}, objective value is {}".format(all_outputs_single[0],all_outputs_single[1]))