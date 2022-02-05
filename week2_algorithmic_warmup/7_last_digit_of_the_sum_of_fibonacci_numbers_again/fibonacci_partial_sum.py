# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10

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
# period_list, period = get_fibonacci_huge_efficient(65, 10)
# print(period)
# print(period_list)
def fibonacci_sum_efficient(from_, to):
    period_list, period = get_fibonacci_huge_efficient(65, 10)
    from_mode = from_ % 60
    to_mode = to % 60
    last_digit_from = period_list[from_mode]
    last_digit_to = period_list[to_mode]

    gap = to - from_
    if gap < period:
        sum_ = 0
        for i in range(from_mode, to_mode + 1):
            sum_ = (sum_ + period_list[i]) % 10
        return sum_

    gap_div, gap_mode = divmod(gap, period)
    # sum_ = 0
    sum_ = (gap_div * sum(period_list)) % 10

    if from_mode <= to_mode:
        for i in range(from_mode, to_mode + 1):
            sum_ = (sum_ + period_list[i]) % 10
        return sum_
    # period_list_number = n % period
    # f_mode_10 = period_list[period_list_number]
    # sum_list = [0]
    # for i in range(len(period_list)):
    #     sum_list.append((sum_list[-1] + period_list[i]) % 10)
    # sum_list = sum_list[1:]
    #
    # sum_list_number = n % len(sum_list)
    if from_mode > to_mode:
        sum_ = (sum(period_list[from_mode:]) + sum(period_list[0:to_mode+1])) % 10
    return sum_

# a = 5618252
# b = 6583591534156
# print(fibonacci_sum_efficient(10, 200))
# print(fibonacci_sum_efficient(a, b))
# period_list, period = get_fibonacci_huge_efficient(65, 10)
# print(period_list[a % 60], a % 60)
# print(period_list[b % 60], b % 60)
# print(divmod(b - a, 60))

if __name__ == '__main__':
    #input = input()
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_sum_efficient(from_, to))
