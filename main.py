import timeit
from functionA import functionA

timeTaken = timeit.timeit(functionA, number = 5) / 5
processPerformance = {"functionA": timeTaken}

print("Finding the element took %f seconds." % processPerformance["functionA"])
