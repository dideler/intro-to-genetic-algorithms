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
from docopt import docopt

class Genotype(object):
    """The population of chromosomes."""

    def __init__(self, population, elite):
        self.population = population
        # TODO: new_pop?
        self.elite = elite

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1')
    print(arguments)
    # TODO
    # read file
    # initialize pop
    # run ga (break down)

# Default crossover is PMX. Can also use CX.
