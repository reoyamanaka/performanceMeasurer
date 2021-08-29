def functionA():
    sampleData = {}
    for i in range(10000000):
        sampleData[i] = i * i
    for i in sampleData.keys():
        if sampleData[i] == 1000000 * 1000000:
            # print("%d found!" % (1000000 * 1000000))
            break
    # print("FunctionA has completed.")
    