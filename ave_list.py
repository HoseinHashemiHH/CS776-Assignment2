
def ave_list(min_fitness):

    # Calculate the average of corresponding elements
    averages = []
    for i in range(len(min_fitness[0])):  # Assuming all inner lists have the same length
        total = 0
        for sublist in min_fitness:
            total += sublist[i]
        avg = total / len(min_fitness)
        averages.append(avg)

    return averages
