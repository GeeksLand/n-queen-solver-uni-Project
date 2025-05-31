# genetic.py
# ----------------
# Solves the N-Queens problem using a Genetic Algorithm.
# It represents each chromosome as a list where the index is the column and the value is the row.
# The algorithm evolves a population of solutions through selection, crossover, and mutation.

import random

def fitness(chromosome):
    clashes = 0
    n = len(chromosome)
    for i in range(n):
        for j in range(i + 1, n):
            if chromosome[i] == chromosome[j] or abs(chromosome[i] - chromosome[j]) == abs(i - j):
                clashes += 1
    return clashes

def crossover(parent1, parent2):
    n = len(parent1)
    point = random.randint(0, n - 1)
    return parent1[:point] + parent2[point:]

def mutate(chromosome, mutation_rate=0.03):
    if random.random() < mutation_rate:
        n = len(chromosome)
        idx = random.randint(0, n - 1)
        chromosome[idx] = random.randint(0, n - 1)
    return chromosome

def generate_chromosome(n):
    return [random.randint(0, n - 1) for _ in range(n)]

def solve_n_queens_genetic(n, population_size=1000, max_generations=2000):
    population = [generate_chromosome(n) for _ in range(population_size)]

    for generation in range(max_generations):
        population = sorted(population, key=lambda c: fitness(c))
        if fitness(population[0]) == 0:
            print(f"Solved in generation {generation}")
            return population[0]

        new_population = population[:10]  # Keep top 10

        while len(new_population) < population_size:
            p1 = random.choice(population[:50])
            p2 = random.choice(population[:50])
            child = crossover(p1, p2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

    print("Failed to find solution")
    return None
