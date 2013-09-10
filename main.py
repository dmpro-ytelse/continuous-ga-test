from problems import MaximizeBitstringGeneticProblem
from solvers import GenerationalGeneticAlgorithmSolver, ContinuousGeneticAlgorithmSolver


def main():
    problem = MaximizeBitstringGeneticProblem(bitstring_length=100)
    print "Solving problem..."
    # output = GenerationalGeneticAlgorithmSolver.solve(problem)
    output = ContinuousGeneticAlgorithmSolver.solve(problem)
    print "Solution found: ", output

main()
