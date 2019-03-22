class Graph:

    def __init__(self, path):

        # Read the graph
        self.array = []
        with open("graph.txt") as f:
            lines = f.readlines()

            for line in lines:
                self.array.append(line.split(" "))

    def costOf(self, genes):
        """ Computes the cost of a gene for the graph """

        cost = int(self.array[genes[0]][genes[len(genes) - 1]])
        # cost = 0
        for i in range(0, len(genes) - 1):
            first = genes[i]
            second = genes[i + 1]
            cost += int(self.array[first][second])
        return cost
