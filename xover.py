# # crossover two parents to create two children
# def crossover(p1, p2, r_cross):
# 	# children are copies of parents by default
# 	c1, c2 = p1.copy(), p2.copy()
# 	# check for recombination
# 	if rand() < r_cross:
# 		# select crossover point that is not on the end of the string
# 		pt = randint(1, len(p1)-2)
# 		# perform crossover
# 		c1 = p1[:pt] + p2[pt:]
# 		c2 = p2[:pt] + p1[pt:]
# 	return [c1, c2]
from numpy.random import rand,randint

def xover(p1, p2, r_cross):
    # Children are copies of parents by default
    c1, c2 = p1.copy(), p2.copy()
    
    # Check for recombination
    if rand() < r_cross:
        # Select two crossover points that are not on the ends of the array
        pt1 = randint(1, len(p1) - 2)
        pt2 = randint(pt1 + 1, len(p1) - 1)
        
        # Perform crossover
        c1 = p1[:pt1] + p2[pt1:pt2] + p1[pt2:]
        c2 = p2[:pt1] + p1[pt1:pt2] + p2[pt2:]
    
    return [c1, c2]

# Example usage:
# p1 and p2 are parent arrays, r_cross is the crossover rate (probability of crossover)
# You can replace p1 and p2 with your actual parent arrays and specify the crossover rate.
# The function will return two children arrays.

# Three-part population crossover
def three_part_crossover(parent1, parent2, parent3):
    num_variables = len(parent1)
    pt1 = randint(1, num_variables - 2)  # First crossover point
    pt2 = randint(pt1, num_variables - 1)  # Second crossover point
    
    child1 = parent1[:pt1] + parent2[pt1:pt2] + parent3[pt2:]
    child2 = parent2[:pt1] + parent3[pt1:pt2] + parent1[pt2:]
    child3 = parent3[:pt1] + parent1[pt1:pt2] + parent2[pt2:]
    
    return child1, child2, child3

# Multi-parent crossover (5-parent crossover)
def five_parent_crossover(parents):
    num_parents = len(parents)
    num_variables = len(parents[0])
    child = [0] * num_variables
    for i in range(num_variables):
        child[i] = sum(parent[i] for parent in parents) / num_parents
    return child