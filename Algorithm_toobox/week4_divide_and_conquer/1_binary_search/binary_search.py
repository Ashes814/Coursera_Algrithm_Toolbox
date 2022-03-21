def binary_search(keys, query):
    low = 0
    high = len(keys) - 1



    while low <= high:
        mid = int(low + (high - low) / 2)
        if query == keys[mid]:
            return mid
        elif query < keys[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1



if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')



# for q in [8, 1, 23, 1, 11]:
#
#     print(binary_search([1,5,8,12,13], q), end=" | ")