import time

processPerformance = {"processA": 0}

sampleData = {}
for i in range(10000000):
    sampleData[i] = i * i

startTime = time.time()

for i in sampleData.keys():
    if sampleData[i] == 1000000 * 1000000:
        print("%d found!" % (1000000 * 1000000))
        break
processPerformance["processA"] = time.time() - startTime

print("Finding the element took %f seconds." % processPerformance["processA"])

