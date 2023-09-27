import random
from objective_functions import f1,f2,f3,f4,f5
def chc_selection(population, objective_func):
    k = 5  # Number of parents to select
    num_vars = len(population[0])  # Number of variables in each individual
    
    # Calculate fitness values for all individuals
    fitness_values = [objective_func(individual) for individual in population]
    
    # Sort the population by fitness values (ascending order)
    sorted_population = [x for _, x in sorted(zip(fitness_values, population))]
    
    # Randomly select 'k' parents from the top 'k' individuals
    parents = random.sample(sorted_population[:k], k)
    
    # Perform uniform crossover to create the child
    child = [random.choice(parents[i]) for i in range(num_vars)]
    
    return child
