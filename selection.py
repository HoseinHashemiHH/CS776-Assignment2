


from numpy.random import rand,randint,uniform
from random import random
# # Roulette wheel selection
# def roulette_wheel_selection(population, scores):
#     total_fitness = sum(scores)
#     r = rand() * total_fitness
#     cumulative_fitness = 0
#     for i, score in enumerate(scores):
#         cumulative_fitness += score
#         if cumulative_fitness >= r:
#             return population[i]
# Random selection
# def random_selection(population):
#     return random.choice(population)
# Rank-based selection
# tournament selection
def selection(pop, scores, k=3):
    selection_ix = randint(len(pop))
    for ix in randint(0, len(pop), k-1):
        if scores[ix] < scores[selection_ix]:
            selection_ix = ix
    return pop[selection_ix]
# def rank_based_selection(population, scores):
#     ranked_population = [x for _, x in sorted(zip(scores, population))]
#     num_individuals = len(ranked_population)
#     selection_probs = [i / num_individuals for i in range(1, num_individuals + 1)]
#     selected_individual = random.choices(ranked_population, weights=selection_probs)[0]
#     return selected_individual