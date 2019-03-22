from ga import GA
import random
from chromosome import Chromosome
from graph import Graph
from crossover import cx, invx, pmx
from mutate import swap, inversion


class TravelingSalesman(GA):
    """ Abstract class, don't run directly """

    def __init__(self, params_path, graph_path, stopping_point):
        GA.__init__(self, params_path)
        self.genes = [i for i in range(0, self.params["NumGenes"])]
        self.graph = Graph(graph_path)
        self.stopping_point = stopping_point

    def init_pop(self):

        for i in range(self.params["NumChromesInit"]):
            # Create a new random gene
            genes = self.genes[:]
            random.shuffle(genes)
            chrome = Chromosome(genes)
            chrome.cost = self.compute_cost(chrome)

            # And add to pop
            self.population.append(chrome)

    def compute_cost(self, chrome):
        return self.graph.costOf(chrome.genes)

    def is_close_enough(self, chrome):
        if self.compute_cost(chrome) <= self.stopping_point:
            return True
        else:
            return False

    def mutate(self):
        mutate_type = self.params["MutateType"]
        if mutate_type == "swap":
            swap.mutate(self)
        elif mutate_type == "inversion":
            inversion.mutate(self)

    def topdown_pair(self):
        pop_clone = list(self.population)  # Clone the list

        pop_clone = pop_clone[:self.params["NumChromes"]]  # Only take the worthy

        # Shuffle the list up
        random.shuffle(pop_clone)

        # Split into two
        left, right = pop_clone[:len(pop_clone) / 2], pop_clone[len(pop_clone) / 2:]

        # Pair the right with the left
        return zip(left, right)

    def k_tournament_pair(self, k):
        tournament = random.sample(self.population, k)
        return min(tournament, key=lambda t: t.cost)

    def tournament_pair(self):
        # create larger population
        size = self.params["NumChromes"]
        mothers = [self.k_tournament_pair(4) for i in range(0, size / 2)]
        fathers = [self.k_tournament_pair(4) for i in range(0, size / 2)]
        return zip(mothers, fathers)

    def mate(self, pairs):
        crossover_type = self.params["CrossoverType"]
        if crossover_type == "pmx":
            self.population = pmx.mate(pairs)
        elif crossover_type == "cx":
            self.population = cx.mate(pairs)
        elif crossover_type == "invx":
            self.population = invx.mate(pairs)

    def pair(self):
        selection_type = self.params["SelectionType"]
        if selection_type == "topdown":
            return self.topdown_pair()
        elif selection_type == "tournament":
            return self.tournament_pair()


class TravelingSalesman_GA(TravelingSalesman):
    pass


class TravelingSalesman_PMX_TopDown(TravelingSalesman):

    def mate(self, pairs):
        self.population = pmx.mate(pairs)

    def pair(self):
        return self.topdown_pair()


class TravelingSalesman_PMX_Tourn(TravelingSalesman):

    def mate(self, pairs):
        self.population = pmx.mate(pairs)

    def pair(self):
        return self.tournament_pair()


class TravelingSalesman_CX_TopDown(TravelingSalesman):

    def mate(self, pairs):
        self.population = cx.mate(pairs)

    def pair(self):
        return self.topdown_pair()


class TravelingSalesman_CX_Tourn(TravelingSalesman):

    def mate(self, pairs):
        self.population = cx.mate(pairs)

    def pair(self):
        return self.tournament_pair()


''' Testing custom crossover operator '''


class TravelingSalesman_INVX_TopDown(TravelingSalesman):

    def mate(self, pairs):
        self.population = invx.mate(pairs)

    def pair(self):
        return self.topdown_pair()


class TravelingSalesman_INVX_Tourn(TravelingSalesman):

    def mate(self, pairs):
        self.population = invx.mate(pairs)

    def pair(self):
        return self.tournament_pair()
