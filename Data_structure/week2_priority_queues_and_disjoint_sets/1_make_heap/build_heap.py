# python3
# import sys
# sys.setrecursionlimit(1000000)#表示递归深度为100w
def Parent(index):
    return int((index + 1) / 2 - 1)


def LeftChild(index):
    return int((index + 1) * 2 - 1)


def RightChild(index):
    return int((index + 1) * 2)


def SiftDown(index, size, data, swaps):
    n = size - 1
    minIndex = index
    left_index = LeftChild(index)
    if left_index <= n and data[left_index] < data[minIndex]:
        minIndex = left_index
    right_index = RightChild(index)
    if right_index <= n and data[right_index] < data[minIndex]:
        minIndex = right_index
    if index != minIndex:
        swaps.append((index, minIndex))
        data[index], data[minIndex] = data[minIndex], data[index]
        SiftDown(minIndex, size, data, swaps)


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    size = len(data)
    # for i in range(len(data)):
    #     for j in range(i + 1, len(data)):
    #         if data[i] > data[j]:
    #             swaps.append((i, j))
    #             data[i], data[j] = data[j], data[i]
    for i in range(int((size - 1 ) / 2) , -1, -1):
        SiftDown(i, size, data, swaps)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)
    # with open('tests/04', 'r') as f:
    #     test_data = f.read().strip().split('\n')
    #     n = int(test_data[0])
    #     data = list(map(int, test_data[1].split(' ')))
    #     assert len(data) == n
    #     f.close()
    # with open('tests/04.a', 'r') as f:
    #     answers = f.read().strip().split('\n')[1:]
    #     f.close()
    # data = [10,9,8,7,6,5,4,3,2,1]
    # n = 10

    # swaps = build_heap(data)
    #
    # print(len(swaps))
    # print(data[0:10])
    # for i, j,in enumerate(swaps):
    #     try:
    #         assert(str(j[0]) + ' ' + str(j[1]) == answers[i])
    #
    #     except:
    #         print(str(j[0]) + ' ' + str(j[1]), end='|')
    #         print(answers[i])


if __name__ == "__main__":
    main()
