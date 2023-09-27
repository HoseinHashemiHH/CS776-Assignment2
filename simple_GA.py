




from numpy.random import rand,randint
from selection import roulette_wheel_selection
from xover import xover
from flip import mutation
from decode import decode
from params import *
from objective_functions import f1,f2,f3,f4,f5
from params import Params_F1,Params_F2,Params_F3,Params_F4,Params_F5
# genetic algorithm search of the one max optimization problem
from numpy.random import randint
from numpy.random import rand



# genetic algorithm
def genetic_algorithm(obj_func, var_num,bounds, n_bits, n_iter, n_pop, r_cross, r_mut):
	# initial population of random bitstring
	pop = [randint(0, 2*var_num, n_bits*len(bounds)).tolist() for _ in range(n_pop)]
	# keep track of best solution
	best, best_eval = 0, obj_func(decode(bounds, n_bits, pop[0]))
	# enumerate generations
	for gen in range(n_iter):
		# decode population
		decoded = [decode(bounds, n_bits, p) for p in pop]
		# evaluate all candidates in the population
		scores = [obj_func(d) for d in decoded]
		# check for new best solution
		for i in range(n_pop):
			if scores[i] < best_eval:
				best, best_eval = pop[i], scores[i]
				print(">%d, new best f(%s) = %f" % (gen,  decoded[i], scores[i]))
		# select parents
		selected = [roulette_wheel_selection(pop, scores) for _ in range(n_pop)]
		# create the next generation
		children = list()
		for i in range(0, n_pop, 2):
			# get selected parents in pairs
			p1, p2 = selected[i], selected[i+1]
			# crossover and mutation
			for c in xover(p1, p2, r_cross):
				# mutation
				mutation(c, r_mut)
				# store for next generation
				children.append(c)
		# replace population
		pop = children
	return [best, best_eval]
obj_func=f1
pobj=Params_F1()
bounds=pobj.bounds_f1
n_bits=pobj.n_bits
n_iter=pobj.n_iter
r_cross=pobj.r_cross
r_mut=pobj.r_mut
n_pop=pobj.n_pop
# perform the genetic algorithm search
best, score = genetic_algorithm(obj_func, bounds, n_bits, n_iter, n_pop, r_cross, r_mut)
print('Done!')
decoded = decode(bounds, n_bits, best)
print('f(%s) = %f' % (decoded, score))


	
	
    