def functionB():
    sampleData = {}
    for i in range(10000000):
        sampleData[i] = i * i
    
    target = sampleData[1000000]
    # print("%d found!" % target)
    # print("FunctionB has completed.")
    