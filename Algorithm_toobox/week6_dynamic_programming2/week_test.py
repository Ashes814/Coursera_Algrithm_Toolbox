def Knapsack(W,n, weight):
    value = [0]
    for w in range(1, W):
        value[w] = 0
        for i in range(1, n):
            if weight[i] <= w:
                val = value[w-weight[i]]+value[i]
                if val > value[w]:
                    value[w] = val
    return value(W)





