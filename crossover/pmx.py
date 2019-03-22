from random import randint
from chromosome import Chromosome


def _subsection(item):
    L = list(range(0, len(item)-1))
    left = randint(0, len(L) - 1)
    right = randint(left + 1, len(L))
    return left, right


def _get_replaced_item(left, right, child, gene, relation_map):

    # Hit a base case
    if gene not in relation_map:
        return gene

    mapped = relation_map[gene]
    if mapped not in child[left:right]:
        return mapped
    else:
        return _get_replaced_item(left, right, child, mapped, relation_map)


def _map(left, right, mother, father):
    return dict(zip(father[left:right], mother[left:right]))


def _getIndex(item, child, left, right):

    # Search left
    for i in range(0, left):
        if child[i] == item:
            return i

    # Search right
    for i in range(right, len(child)):
        if child[i] == item:
            return i


def _swap_leftover_genes(left, right, mothers_child, fathers_child):
    father_map = _map(left, right, mothers_child, fathers_child)

    # Swap left versions
    for i in range(0, left):
        gene = fathers_child[i]
        if gene not in father_map:
            continue
        mother_gene = _get_replaced_item(left, right, fathers_child, gene, father_map)

        fathers_child[i] = mother_gene
        m_index = _getIndex(mother_gene, mothers_child, left, right)
        mothers_child[m_index] = gene

    for i in range(right, len(fathers_child)):
        gene = fathers_child[i]
        if gene not in father_map:
            continue
        mother_gene = _get_replaced_item(left, right, fathers_child, gene, father_map)

        fathers_child[i] = mother_gene
        m_index = _getIndex(mother_gene, mothers_child, left, right)
        mothers_child[m_index] = gene

    return fathers_child, mothers_child


def _mate_one(pair):
    mother, father = pair
    left, right = _subsection(mother)

    # Create copies (children) so we don't effect the original
    mothers_child = list(mother.genes)
    fathers_child = list(father.genes)

    # Step 1, swap the sides

    mothers_child[left:right] = father.genes[left:right]
    fathers_child[left:right] = mother.genes[left:right]

    # Step 2, deal with the leftovers
    fathers_child, mothers_child = _swap_leftover_genes(left, right, mothers_child, fathers_child)

    child1_chrome = Chromosome(mothers_child)
    child2_chrome = Chromosome(fathers_child)

    return child1_chrome, child2_chrome


def mate(pairs):
    people = []
    for mother, father in pairs:
        child1, child2 = _mate_one((mother, father))
        people += [mother, father, child1, child2]
    return people
