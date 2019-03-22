from traveling_salesman import *
import parameters

param_path = 'params.json'


def test(genetic):
    n = 1
    full_cost = 0
    full_iterations = 0
    for i in range(0, n):
        ga = genetic(param_path, 'graph.txt', 2020)
        ga.init_pop()
        ga.sort()

        iterations, chrome = ga.evolve()
        # print 'total iterations:', iterations, 'chrome:', chrome, 'cost:', chrome.cost,
        full_cost += chrome.cost
        full_iterations += iterations

    print 'Average cost:', full_cost / n, "Iterations:", full_iterations / n


params = parameters.read(param_path)
print "Crossover:", params["CrossoverType"].upper(), "\nSelection:", params["SelectionType"].upper(), "\nMutation:", \
    params["MutateType"].upper()
test(TravelingSalesman_GA)
print '\n'

# print "Testing PMX with Tournament"
# test(TravelingSalesman_PMX_Tourn)
# print '\n'
#
# print "Testing PMX with Top Down"
# test(TravelingSalesman_PMX_TopDown)
# print '\n'
#
# print "Testing Cycle CX with Tournament"
# test(TravelingSalesman_CX_Tourn)
# print '\n'
#
# print "Testing Cycle CX with TopDown"
# test(TravelingSalesman_CX_TopDown)
# print '\n'
#
#
# ''' Testing custom crossover operator '''
#
#
# print "Testing INVX with TopDown"
# test(TravelingSalesman_INVX_TopDown)
# print '\n'
#
# print "Testing INVX with Tournament"
# test(TravelingSalesman_INVX_Tourn)
# print '\n'
