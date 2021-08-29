import timeit
from functionA import functionA
from functionB import functionB


RUNS = 3

timeTakenA = timeit.timeit(functionA, number = RUNS) / RUNS
timeTakenB = timeit.timeit(functionB, number = RUNS) / RUNS

processPerformance = {"functionA": timeTakenA, "functionB": timeTakenB}

print("functionA took %f seconds and functionB took %f seconds." % (processPerformance["functionA"], processPerformance["functionB"]))

shorter = "functionA"

if processPerformance["functionA"] > processPerformance["functionB"]:
    shorter = "functionB"

print("From an average of %d runs, %s took less time to complete." % (RUNS, shorter))
