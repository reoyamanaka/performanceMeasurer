import time
from functionA import functionA

processPerformance = {"functionA": 0}
startTime = time.time()

functionA()

processPerformance["functionA"] = time.time() - startTime

print("Finding the element took %f seconds." % processPerformance["functionA"])

