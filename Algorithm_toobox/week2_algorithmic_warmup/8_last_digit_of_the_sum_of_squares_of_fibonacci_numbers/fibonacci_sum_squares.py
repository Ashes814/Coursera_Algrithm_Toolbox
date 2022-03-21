# Uses python3
from sys import stdin
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

    # period_list_number = n % period
    return period_list, period

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def fibonacci_sum_squares_efficient(n):
    period_list, period = get_fibonacci_huge_efficient(65, 10)
    if n == 0:
        return 0
    return (period_list[n % period] * ((period_list[n % period] + period_list[(n -1) % period])%10))%10



# for i in [7, 73, 1234567890]:
#     print(fibonacci_sum_squares_efficient(i))




if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_efficient(n))
