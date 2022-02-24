import time
import math
money = 28
coins = [20, 8, 1]
# def GreedyChange(money, coins):
#
#     changes = []
#     while money > 0:
#         for coin in coins:
#             if money >= coin:
#                 changes.append(coin)
#                 money -= coin
#                 break
#
#     return len(changes)
#
# # t0 = time.time()
# print(GreedyChange(money, coins))
# # print(time.time() - t0)
#

# def RecursiveChange(money, coins):
#     if money == 0:
#         return 0
#     min_num_coins = math.inf
#     for coin in coins:
#         if money >= coin:
#             num_coins = RecursiveChange(money - coin, coins)
#             if num_coins + 1 < min_num_coins:
#                 min_num_coins = num_coins + 1
#
#     return min_num_coins
#
#
# t0 = time.time()
# print(RecursiveChange(money, coins))
# print(time.time() - t0)


#
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
print(DPChange(money, coins))
# print(time.time() - t0)



