# Uses python3
import sys
def gcd_efficient(a, b):

    if min(a,b):


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b



def lcm_efficient(a, b):
    pass

if __name__ == '__main__':
    # input = sys.stdin.read()
    input = input()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

