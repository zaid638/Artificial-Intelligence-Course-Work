from GA_code import generate_population, roulette_wheel_selection, crossover, mutate


# Knapsack problem setup
items = [
    {"weight": 2, "value": 3},
    {"weight": 3, "value": 4},
    {"weight": 4, "value": 5},
    {"weight": 5, "value": 8},
]
knapsack_capacity = 9

# Fitness function for knapsack problem
def knapsack_fitness(chromosome):
    total_weight = 0
    total_value = 0
    for i, bit in enumerate(chromosome):
        if bit == '1':
            total_weight += items[i]["weight"]
            total_value += items[i]["value"]
    # Penalize if weight exceeds capacity
    if total_weight > knapsack_capacity:
        return 0  # Invalid solution
    return total_value

# Decode binary string for knapsack (already binary, so this is just casting)
def decode_chromosome_knapsack(chromosome):
    return chromosome

# Main GA process for knapsack problem
def genetic_algorithm_knapsack(pop_size, gene_length, generations, crossover_rate, mutation_rate):
    population = generate_population(pop_size, gene_length)
    for generation in range(generations):
        # Evaluate fitness
        fitnesses = [knapsack_fitness(decode_chromosome_knapsack(chrom)) for chrom in population]

        # Log current generation
        print(f"Generation {generation}:")
        print(f"Population: {population}")
        print(f"Fitnesses: {fitnesses}")
        print()

        # Select parents and generate new population
        new_population = []
        for _ in range(pop_size // 2):
            parent1 = roulette_wheel_selection(population, fitnesses)
            parent2 = roulette_wheel_selection(population, fitnesses)
            offspring1, offspring2 = crossover(parent1, parent2, crossover_rate)
            new_population.extend([mutate(offspring1, mutation_rate), mutate(offspring2, mutation_rate)])
        
        population = new_population
    
    # Final population
    fitnesses = [knapsack_fitness(decode_chromosome_knapsack(chrom)) for chrom in population]
    best_solution = max(zip(population, fitnesses), key=lambda x: x[1])
    print(f"Final Best Solution: Chromosome: {best_solution[0]}, Fitness: {best_solution[1]}")

# Run the simulation for knapsack
genetic_algorithm_knapsack(pop_size=6, gene_length=len(items), generations=10, crossover_rate=0.8, mutation_rate=0.1)
