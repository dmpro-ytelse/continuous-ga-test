import random


class MaximizeBitstringGeneticProblem(object):

    def __init__(self, bitstring_length=500):
        self.bitstring_length = bitstring_length

    def select(self, population):
        if(len(population) < 10):
            return max(zip(map(self.fitness, population), population))[1]
        return max(
            self.select(population[:len(population)/2]),
            self.select(population[len(population)/2:])
        )

    def crossover(self, individual_a, individual_b):
        return individual_a[:len(individual_a)/2] + \
            individual_b[len(individual_b)/2:]

    def mutate(self, individual):
        return [bit ^ 1 if random.random() > 0.95 else bit
                for bit in individual]

    def createIndividual(self):
        return [int(random.random() * 2) for i in range(self.bitstring_length)]

    def fitness(self, population):
        return float(sum(population))/len(population)
