import random

# Objective function
def fitness_function(x):
    return x ** 2

# Generate random initial population
def generate_population(size, gene_length):
    return [''.join(random.choice('01') for _ in range(gene_length)) for _ in range(size)]

# Decode binary string to integer
def decode_chromosome(chromosome):
    return int(chromosome, 2)

# Select parents using roulette wheel selection
def roulette_wheel_selection(population, fitnesses):
    total_fitness = sum(fitnesses)
    pick = random.uniform(0, total_fitness)
    current = 0
    for i, fitness in enumerate(fitnesses):
        current += fitness
        if current > pick:
            return population[i]

# Perform crossover
def crossover(parent1, parent2, crossover_rate):
    if random.random() < crossover_rate:
        point = random.randint(1, len(parent1) - 1)
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]
    return parent1, parent2

# Perform mutation
def mutate(chromosome, mutation_rate):
    chromosome = list(chromosome)
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = '1' if chromosome[i] == '0' else '0'
    return ''.join(chromosome)

# Main GA process
def genetic_algorithm(pop_size, gene_length, generations, crossover_rate, mutation_rate):
    population = generate_population(pop_size, gene_length)
    for generation in range(generations):
        # Decode and evaluate fitness
        decoded_population = [decode_chromosome(chrom) for chrom in population]
        fitnesses = [fitness_function(x) for x in decoded_population]

        # Log current generation
        print(f"Generation {generation}:")
        print(f"Population: {population}")
        print(f"Decoded: {decoded_population}")
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
    decoded_population = [decode_chromosome(chrom) for chrom in population]
    fitnesses = [fitness_function(x) for x in decoded_population]
    best_solution = max(zip(population, decoded_population, fitnesses), key=lambda x: x[2])
    print(f"Final Best Solution: Chromosome: {best_solution[0]}, Value: {best_solution[1]}, Fitness: {best_solution[2]}")

# Run the simulation
genetic_algorithm(pop_size=4, gene_length=5, generations=5, crossover_rate=0.8, mutation_rate=0.1)
