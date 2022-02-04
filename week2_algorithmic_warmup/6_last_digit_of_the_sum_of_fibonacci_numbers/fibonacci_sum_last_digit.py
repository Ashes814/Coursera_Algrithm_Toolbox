# Uses python3
import sys
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


def fibonacci_sum_efficient(n):
    period_list, period = get_fibonacci_huge_efficient(65, 10)
    # period_list_number = n % period
    # f_mode_10 = period_list[period_list_number]
    sum_list = [0]
    for i in range(len(period_list)):
        sum_list.append((sum_list[-1] + period_list[i]) % 10)
    sum_list = sum_list[1:]

    sum_list_number = n % len(sum_list)

    return sum_list[sum_list_number]

# def fibonacci_sum_naive(n):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current  = 1
#     _sum      = 1
#
#     for _ in range(n - 1):
#         previous, current = current, (previous + current) % 10
#         _sum = (_sum + current) % 10
#
#     return _sum
#
# print(fibonacci_sum_efficient(100))
#
# for i in range(100):
#     print(fibonacci_sum_naive(i), end=' ')


if __name__ == '__main__':
    #input = sys.argv[1]
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_efficient(n))
