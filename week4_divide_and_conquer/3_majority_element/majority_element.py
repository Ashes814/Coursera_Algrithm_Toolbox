# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    write your code here
    count_element = {}
    for number in a:
        n = str(number)
        count_element[n] = count_element.get(n, 0) + 1

    for key in count_element.keys():
        if count_element[key] > (len(a) / 2):
            return 1

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

# print(get_majority_element([2,3,9,2,2], 0, 5))
#
# print(get_majority_element([1,2,3,4], 0, 3))