import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci_huge_efficient(n, m):
    if n == 0:
        return 0


    period = 0
    period_list = []

    previous = 0
    current  = 1

    for i in range(n-1):
        period_list.append(previous % m)
        previous, current = current, previous + current
        period += 1
        if previous % m == 0 and current % m == 1:
            break
    else:
        return current % m

    period_list_number = n % period
    print(period, period_list)
    return

get_fibonacci_huge_efficient(100, 10)