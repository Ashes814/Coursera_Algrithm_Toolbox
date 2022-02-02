# Uses python3
import time
# def calc_fib1(n):
#     if (n <= 1):
#         return n
#
#     return calc_fib1(n - 1) + calc_fib1(n - 2)


def calc_fib2(n):
    if (n <= 1):
        return n

    res = [0, 1]
    for i in range(n-1):
        res_temp = res[1]
        res[1] = res[0] + res[1]
        res[0] = res_temp

    return res[1]


n = int(input())
# t0 = time.time()
# print(calc_fib1(n))
# print(time.time() - t0)

t1 = time.time()
print(calc_fib2(n))
print(time.time() - t1)
