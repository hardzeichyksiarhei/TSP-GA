from random import randint
from chromosome import Chromosome


def _subsection(item):
    L = list(range(0, len(item) - 1))
    left = randint(0, len(L) - 1)
    right = randint(left + 1, len(L))
    return left, right


def _map(mother, father):
    return dict(zip(father, mother))


def _get_cycle(start, relation_map):
    cycle = [start]

    current = relation_map[start]
    while current not in cycle:
        cycle.append(current)
        current = relation_map[current]

    return cycle


def _superimpose_cycle(child, cycle):
    c = 0

    for i in range(0, len(child)):
        if child[i] in cycle:
            child[i] = cycle[c]
            c += 1
    return child


def _mate_one(pair):
    mother, father = pair
    left, right = _subsection(mother)

    # Create copies (children) so we don't effect the original
    mothers_child = list(mother.genes)
    fathers_child = list(father.genes)

    relation_map = _map(mothers_child, fathers_child)
    cycle = _get_cycle(fathers_child[0], relation_map)

    mothers_child = _superimpose_cycle(mothers_child, cycle)
    fathers_child = _superimpose_cycle(fathers_child, cycle)

    child1_chrome = Chromosome(mothers_child)
    child2_chrome = Chromosome(fathers_child)

    return child1_chrome, child2_chrome


def mate(pairs):
    people = []
    for mother, father in pairs:
        child1, child2 = _mate_one((mother, father))
        people += [mother, father, child1, child2]
    return people
