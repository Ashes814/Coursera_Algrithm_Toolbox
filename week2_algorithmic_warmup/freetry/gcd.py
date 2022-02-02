# Find the Greatest Common Divisor (GCD) of two numbers
import sys
import time

#Very slow
def naive_gcd(number1, number2):

    best = 0
    for n in range(1, min(number1, number2) + 1):
        if number1 % n == 0 and number2 % n == 0:
            best = n
    return best

#Efficitent
#欧几里得算法
def efficient_gcd(number1, number2):
    mode = max(number1, number2) % min(number1, number2)
    if mode == 0:
        return min(number1, number2)

    return efficient_gcd(min(number1, number2), mode)






if __name__ == '__main__':
    number1 = int(sys.argv[1])
    number2 = int(sys.argv[2])

    t0 = time.time()
    print('GCD: '+ str(naive_gcd(number1, number2)))
    t1 = time.time() - t0
    print('naive algorithm running time: ' + str(t1))

    t2 = time.time()
    print('GCD: '+ str(efficient_gcd(number1, number2)))
    t3 = time.time() - t2
    print('efficient algorithm running time: ' + str(t3))

