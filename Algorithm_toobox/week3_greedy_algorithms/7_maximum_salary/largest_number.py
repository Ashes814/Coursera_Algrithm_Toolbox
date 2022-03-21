#Uses python3

import sys


def isGreaterOrEqual(digit, maxDigit):
    forward = int(str(digit) + str(maxDigit))
    reverse = int(str(maxDigit) + str(digit))

    if forward >= reverse:
        return True
    else:
        return False


def largest_number(digits):
    salary = []

    while len(digits) > 0:
        maxDigit = 0
        for digit in digits:
            if isGreaterOrEqual(digit, maxDigit):
                maxDigit = digit

        salary.append(maxDigit)
        digits.remove(maxDigit)
    number = ''
    for i in salary:
        number += str(i)
    number = int(number)
    return number

# def largest_number(a):
#     #write your code here
#     res = ""
#     for x in a:
#         res += x
#     return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
# print(largest_number([21, 2]))
#
# print(largest_number([9, 9, 1, 6, 4]))
# print(largest_number([23,39,92]))
# print(largest_number([2,3,9]))
# print(largest_number([6,61,68]))
# print(largest_number([4,42,46,427,465]))
# print(largest_number([5,52,57,517,532,569,581]))