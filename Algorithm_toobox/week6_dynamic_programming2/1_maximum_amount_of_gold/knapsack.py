# Uses python3
import sys


def optimal_weight(W, w):
    # write your code here
    n = len(w)
    w = [0] + w
    value = [[0 for i in range(n + 1)] for j in range(W + 1)]
    for i in range(1, n + 1):
        for weight in range(1, W + 1):
            value[weight][i] = value[weight][i - 1]
            if w[i] <= weight:
                val = value[weight - w[i]][i - 1] + w[i]
                if value[weight][i] < val:
                    value[weight][i] = val

    # result = 0
    # for x in w:
    #     if result + x <= W:
    #         result = result + x
    return max(max(value))


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))


# print(optimal_weight(10, [1,4,8]))
# print(optimal_weight(20, [5,7,12,18]))