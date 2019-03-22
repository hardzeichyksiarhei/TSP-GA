import random


def mutate(self):
    how_many = int(len(self.population) * self.params["MutFact"])

    for chrome in random.sample(self.population, how_many):
        # Pick a random gene to mutate
        x = random.randint(0, self.params["NumGenes"] - 1)
        y = random.randint(0, self.params["NumGenes"] - 1)
        chrome.genes[x], chrome.genes[y] = chrome.genes[y], chrome.genes[x]
        chrome.cost = self.compute_cost(chrome)
