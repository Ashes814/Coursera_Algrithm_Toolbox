# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


#Efficitent
#欧几里得算法
def efficient_gcd(number1, number2):
    mode = max(number1, number2) % min(number1, number2)
    if mode == 0:
        return min(number1, number2)

    return efficient_gcd(min(number1, number2), mode)



if __name__ == "__main__":
    # input = sys.stdin.read()
    input = input()
    a, b = map(int, input.split())
    print(efficient_gcd(a, b))
