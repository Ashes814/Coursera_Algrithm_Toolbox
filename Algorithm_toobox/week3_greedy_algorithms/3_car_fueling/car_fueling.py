# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    numRefills, currentRefill = 0, 0
    n = len(stops)
    stops = [0] + stops + [distance]
    while currentRefill <= n:
        lastRefill = currentRefill

        while (currentRefill <= n) and ((stops[currentRefill + 1] - stops[lastRefill]) <= tank):
            currentRefill += 1
        if lastRefill == currentRefill:
            return -1

        if currentRefill <= n:
            numRefills += 1

    return numRefills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))

#
# print(compute_min_refills(950, 400, [200,375,550,750]))
#
# print(compute_min_refills(10, 3, [1,2,5,79]))