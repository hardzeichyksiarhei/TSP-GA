from random import randint
from chromosome import Chromosome


def inversion(perm):
    n = len(perm)

    inv = [0] * n

    for i in range(0, n):
        m = 0
        while perm[m] != i:
            if perm[m] > i:
                inv[i] = inv[i] + 1
            m = m + 1

    return inv


def permutation(inv):
    n = len(inv)

    pos = [0] * n
    perm = [0] * n

    for i in range(n, 0, -1):
        for m in range(i, n):
            if pos[m] >= inv[i - 1] + 1:
                pos[m] = pos[m] + 1
        pos[i - 1] = inv[i - 1] + 1

    for i in range(0, n):
        perm[pos[i] - 1] = i

    return perm


def _mate_one(pair):
    mother, father = pair
    n = len(mother)

    inv1 = inversion(list(mother.genes))
    inv2 = inversion(list(father.genes))

    line = randint(0, n - 1)

    new_inv1 = inv1[0:line] + inv2[line:n]
    new_inv2 = inv2[0:line] + inv1[line:n]

    # line1 = randint(0, n - 1)
    # line2 = randint(0, n - 1)
    #
    # if line1 > line2:
    #     line1, line2 = line2, line1
    #
    # new_inv1 = inv2[0:line1] + inv1[line1:line2] + inv2[line2:n]
    # new_inv2 = inv1[0:line1] + inv2[line1:line2] + inv1[line2:n]

    child1 = permutation(new_inv1)
    child2 = permutation(new_inv2)

    child1_chrome = Chromosome(child1)
    child2_chrome = Chromosome(child2)

    return child1_chrome, child2_chrome


def mate(pairs):
    people = []
    for mother, father in pairs:
        child1, child2 = _mate_one((mother, father))
        people += [mother, father, child1, child2]
    return people
