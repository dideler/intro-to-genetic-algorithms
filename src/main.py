#!/usr/bin/env python

"""Simple Genetic Algorithm for solving TSP.

Usage:
  main.py FILE --pop-size=POP_SIZE --max-gen=MAX_GENERATIONS --xover-rate=CROSSOVER_RATE --mute-rate=MUTATION_RATE --num-elites=NUM_ELITES --tournament-k=K
  main.py (-h | --help)
  main.py (-v | --version)

Options:
  -h --help     Show this screen.
  -v --version  Show version.

"""
from collections import OrderedDict
import random

from docopt import docopt

class Genotype(object):
    """The population of chromosomes."""

    def __init__(self):
        self.population = []
        self.new_pop = []
        self.elite = []

class Chromosome(object):
    """TODO"""
    pass

class GA(object):
    """A mix and match of stuff for the GA. Don't judge my messy code, was in a rush."""
    # TODO: Do we *need* a clas for this?
    def __init__(self, args):
        self.args = args
        self.cities = []
        self.solutions = []  # aka population/genotype - 2D list: [solution_index][city_index]

    def run(self):
        """Runs the GA.

        1. Read data
        2. Initialize population
        3. ...
        """
        self._get_cities_from_file(self.args['FILE'])
        self._init_population()
        self._loop()

    def _get_cities_from_file(self, filepath):
        with open(filepath) as f:
            # There are 6 lines at the top of the file that we don't care about.
            [next(f) for _ in xrange(6)]

            for line in f:
                city_num, x, y = map(int, line.split())
                self.cities.append((x,y))
                print "{}: x={}, y={}".format(city_num, x, y)

    def _init_population(self):
        """Creates a random population of legal chromosomes.

        Or in other words, let's start with a bunch of random solutions.
        """
        solution = [i for i in xrange(1, len(self.cities) + 1)]  # aka chromosome

        for _ in xrange(self.args['--pop-size']):
            random.shuffle(solution)
            self.solutions.append(solution)

    def _loop(self):
        """The main loop of the GA.

        Algorithm:

            Evaluate fitness of every solution

            For every generation:  # Stopping criteria can also be threshold for fitness level, time based, and so on.
                Evaluate fitness of every solution
                Calculate population fitness (i.e. average fitness)

                While new population is not full:
                    Select parents (using tournament selection)
                    Apply crossover with probability Pc (produces two children, or copy parents if crossover not applied)
                    Apply mutation with probability Pm to offspring (if mutation not applied, no changes)

                Copy elite(s) into new population
                Replace old population with new population
                Evaluate fitness of every solution
        """
        pass

    def _find_elite(self):
        """TODO"""
        pass

    def _tournament_selection(self):
        """Selects a chromosome that will be used to reproduce (i.e. parent).

        Select k chromosomes randomly, from those, select the best.
         You may want to allow selecting the same parent twice for mating.
         Happens in nature with certain species.

        TODO
        """
        pass

    def _crossover(self):
        """TODO

        Special crossovers exist for ordered chromosomes (i.e. order matters in the solution).

        Partially matched crossover (PMX):
            Two crossover points selected at random.
            Points give matching selection. Parents are "mapped" to each other.
            http://www.emeraldinsight.com/content_images/fig/0680230702015.png

        Cycle crossover (CX):
            Each element comes from one parent together with its position.
            Genes selected for inheritance is based on a cycle of connecting genes.
            Cycle starts with the first gene from the first parent.
            Cycle ends when the last gene inherited is connected to the first gene inherited.
            http://www.cs.vu.nl/~gusz/ecbook/figures/3-17.jpg

        Other types: http://www.obitko.com/tutorials/genetic-algorithms/crossover-mutation.php"""
        pass

    def _mutation(self):
        """TODO

        Reciprocal Exchange Mutation (REM):
            Swaps two arbitrary genes in the offspring.

            Choose two arbitrary unique genes.
            Select some offspring (e.g. last two).
        """
        pass

    def _evaluate(self):
        """Evaluates the fitness of a chromosome.

        Fitness is measured in total distance, which is calculated as Euclidean distance (aka straight line).
        The lower the distance, the better the fitness (since TSP is a minimization problem).

        distance = sqrt( (x2 - x1)^2 + (y2 - y1)^2 )
        """
        pass

def _string_to_num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def cast_args(args):
    """The numbers are stored as strings via doctopt. Convert them to numbers."""
    for key, val in args.items():
        if key.startswith('--') and isinstance(val, str):
            args[key] = _string_to_num(val)

if __name__ == '__main__':
    args = docopt(__doc__, version='0.1')
    cast_args(args)
    print args
    GA(args).run()

# Default crossover is PMX. Can also use CX.
