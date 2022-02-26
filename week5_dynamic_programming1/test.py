import math
money = 28
coins = [20, 8, 1]
def GreedyChange(money, coins):

    changes = []
    while money > 0:
        for coin in coins:
            if money >= coin:
                changes.append(coin)
                money -= coin
                break

    return len(changes)

# t0 = time.time()
# print(GreedyChange(money, coins))
# print(time.time() - t0)


def RecursiveChange(money, coins):
    if money == 0:
        return 0
    min_num_coins = math.inf
    for coin in coins:
        if money >= coin:
            num_coins = RecursiveChange(money - coin, coins)
            if num_coins + 1 < min_num_coins:
                min_num_coins = num_coins + 1

    return min_num_coins

#
# t0 = time.time()
# print(RecursiveChange(money, coins))
# print(time.time() - t0)



def DPChange(money, coins):
    min_num_coins = [0] * (money + 1)
    for m in range(1, money + 1):
        min_num_coins[m] = float('inf')
        for coin in coins:
            if m >= coin:
                num_coins = min_num_coins[m - coin] + 1
                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins
    return min_num_coins[money]

# t0 = time.time()
# print(DPChange(money, coins))
# print(time.time() - t0)

def EditDistance(wordA, wordB):
    n = len(wordA)
    m = len(wordB)

    D = []
    for i in range(n + 1):
        D.append([])
        for j in range(m + 1):
            D[i].append(0)
    for i in range(n + 1):
        D[i][0] = i
    for j in range(m + 1):
        D[0][j] = j

    for j in range(1, m + 1):
        for i in range(1, n + 1):
            insertion = D[i][j - 1] + 1
            deletion = D[i - 1][j] + 1
            match = D[i - 1][j - 1]
            mismatch = D[i - 1][j - 1] + 1

            if wordA[i - 1] == wordB[j - 1]:
                D[i][j] = min(insertion, deletion, match)
            else:
                D[i][j] = min(insertion, deletion, mismatch)
    OutputAlignment(wordA,wordB,D, n-1, m-1)
    return D

#Backtracking
def OutputAlignment(A,B,D, i, j):
    if i == -1 and j == -1:
        return

    if i > 0 and D[i][j] == D[i - 1][j] + 1:
        OutputAlignment(A,B,D, i-1, j)
        print(A[i], '-')
    elif j > 0 and D[i][j] == D[i][j - 1] + 1:
        OutputAlignment(A,B,D, i, j-1)
        print('-', B[j])
    else:
        OutputAlignment(A,B,D, i-1, j-1)
        print(A[i], B[j])


print(EditDistance(['a','b','c','e'], ['a','b','d','e']))




