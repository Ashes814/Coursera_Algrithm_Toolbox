# Uses python3
import sys
def efficient_gcd(number1, number2):
    mode = max(number1, number2) % min(number1, number2)
    if mode == 0:
        return min(number1, number2)

    return efficient_gcd(min(number1, number2), mode)


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b



def lcm_efficient(a, b):
    gcd = efficient_gcd(a, b)

    return int(a/gcd * b/gcd * gcd)

if __name__ == '__main__':
    input = sys.stdin.read()
    #input = input()
    a, b = map(int, input.split())
    print(lcm_efficient(a, b))

