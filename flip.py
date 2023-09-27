# mutation operator
from numpy.random import rand,randint
import numpy as np
# Mutation (Gaussian mutation)
def mutate(solution, mutation_rate, mutation_scale, bounds):
    mutated_solution = []
    for i, gene in enumerate(solution):
        if rand() < mutation_rate:
            mutation = np.random.normal(loc=0, scale=mutation_scale)
            mutated_gene = gene + mutation
            # Ensure the mutated gene stays within bounds
            mutated_gene = max(bounds[i][0], min(bounds[i][1], mutated_gene))
            mutated_solution.append(mutated_gene)
        else:
            mutated_solution.append(gene)
    return mutated_solution