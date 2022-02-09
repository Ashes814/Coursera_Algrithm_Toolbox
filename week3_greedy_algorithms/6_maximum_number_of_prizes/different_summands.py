# Uses python3
import sys

def optimal_summands(n):
    summands = []
    choices = [number for number in range(1, n+1)]
    current = 0
    #write your code here
    while n > 0:
        n = n - choices[current]
        if n > 0 and n > choices[current]:
            summands.append(choices[current])
            current += 1
        else:
            summands.append(n + choices[current])
            break
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
# print(optimal_summands(2))
# print(optimal_summands(6))
# print(optimal_summands(8))
# print(optimal_summands(22))