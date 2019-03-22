import random


def mutate(self):
    how_many = int(len(self.population) * self.params["MutFact"])

    for chrome in random.sample(self.population, how_many):
        # Pick a random gene to mutate
        x = random.randint(0, self.params["NumGenes"] - 1)
        y = random.randint(0, self.params["NumGenes"] - 1)
        if x > y:
            x, y = y, x
        genes = chrome.genes
        first = genes[0:x]
        middle = genes[x:y]
        last = genes[y:len(genes)]
        new_genes = first + middle[::-1] + last
        chrome.genes = new_genes
        chrome.cost = self.compute_cost(chrome)
