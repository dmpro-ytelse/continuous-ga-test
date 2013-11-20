

class GenerationalGeneticAlgorithmSolver(object):

    @staticmethod
    def solve(problem, fitness_goal=0.95, population_size=100):

        # population size has to be a multiple of 4 for implementation reasons
        population_size = population_size - population_size % 4

        # generate initial population
        population = sorted(
            [problem.createIndividual() for i in range(population_size)],
            key=lambda individual: 1 - problem.fitness(individual))

        generation = 0

        best_individual = population[0]

        while problem.fitness(best_individual) < fitness_goal:

            print "generation", generation
            print "fitness:", problem.fitness(best_individual)
            print ""

            # possibly store new best individual
            if problem.fitness(population[0]) > problem.fitness(
                    best_individual):
                best_individual = population[0]

            # select
            selected = [problem.select(population)
                        for i in range(population_size/2)]

            # crossover
            new_individuals = [problem.crossover(
                               selected[i*2], selected[i*2+1])
                               for i in range(len(selected)/2)]

            # mutate
            mutated_new_individuals = [problem.mutate(individual)
                                       for individual in new_individuals]

            # replace least fit individuals with new individuals
            population.sort(
                key=lambda individual: 1 - problem.fitness(individual))
            population = population[:population_size*3/4] + \
                mutated_new_individuals

            population.sort(
                key=lambda individual: 1 - problem.fitness(individual))

            generation += 1

        return {
            "solution": best_individual,
            "fitness": problem.fitness(best_individual),
            "work": generation,
        }


class ContinuousGeneticAlgorithmSolver(object):

    @staticmethod
    def solve(problem, fitness_goal=0.95, population_size=100):

        # generate initial population
        population = [problem.createIndividual()
                      for i in range(population_size)]

        work = 0

        best_individual = max(reversed(sorted(zip(map(
            problem.fitness, population), population))))[1]

        place_counter = 0

        while problem.fitness(best_individual) < fitness_goal:

            print "work", work
            print "fitness:", problem.fitness(best_individual)
            print ""

            # select
            selected_a = problem.select(population)
            selected_b = problem.select(population)

            # crossover
            new_individual = problem.crossover(selected_a, selected_b)

            # mutate
            mutated_new_individual = problem.mutate(new_individual)

            # replace random individual with new individual
            population[place_counter] = mutated_new_individual
            place_counter = (place_counter + 1) % len(population)

            if problem.fitness(mutated_new_individual) > problem.fitness(
                    best_individual):
                best_individual = mutated_new_individual

            work += 1

        return {
            "solution": best_individual,
            "fitness": problem.fitness(best_individual),
            "work": work,
        }
