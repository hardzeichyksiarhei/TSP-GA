from ga import GA
import random
from chromosome import Chromosome

def hamming_distance(x, y):
    """ Computes the distance between two strings """
    assert len(x) == len(y)
    return sum(ch1 != ch2 for ch1, ch2 in zip(x, y))

class WordGuess(GA):

    def __init__(self, params_path, target):
        GA.__init__(self, params_path)
        self.target = target

    def mate(self, pairs):
        """ Mates """
        families = [] # Build us some real estate
        for mother, father in pairs:
            i = random.randint(0, self.params["NumGenes"])

            # Create new children
            child1 = Chromosome(''.join(mother.genes[:i] + father.genes[i:]))
            child1.cost = self.compute_cost(child1)
            child2 = Chromosome(''.join(mother.genes[i:] + father.genes[:i]))
            child2.cost = self.compute_cost(child2)

            # Add a happy new family
            families += [child1, child2, mother, father]

        self.population = families # Create new families

    def pair(self):
        """ Pairs randomly """
        pop_clone = list(self.population) # Clone the list

        pop_clone = pop_clone[:self.params["NumChromes"]] # Only take the worthy

        # Shuffle the list up
        random.shuffle(pop_clone)

        # Split into two
        left, right = pop_clone[:len(pop_clone)/2], pop_clone[len(pop_clone)/2:]

        # Pair the right with the left
        return zip(left, right)

    def is_close_enough(self, chrome):
        """ Should be overwritten by subclass """
        if self.compute_cost(chrome) == 0:
            return True
        else:
            return False

    def compute_cost(self, chrome):
        """ Should be overwritten by subclass, computes the cost of a single chromosome """
        return hamming_distance(self.target, str(chrome))


ga = WordGuess("params.json", "honey")
ga.init_pop()
ga.sort()
print ga.evolve()
