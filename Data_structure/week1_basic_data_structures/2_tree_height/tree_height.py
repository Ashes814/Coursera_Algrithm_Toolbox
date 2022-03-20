# python3

import sys
import threading

def height(tree, root):
    if tree[root] == []:
        return 0
    max_height = 0
    for r in range(len(tree[root])):
        update_height = height(tree, tree[root][r])
        if update_height > max_height:
            max_height = update_height


    return max_height + 1
def compute_height(n, parents):
    # Replace this code with a faster implementation
    # max_height = 0
    # for vertex in range(n):
    #     height = 0
    #     current = vertex
    #     while current != -1:
    #         height += 1
    #         current = parents[current]
    #     max_height = max(max_height, height)
    nodes = [[] for i in range(n)]
    for child_index in range(n):
        parent_index = parents[child_index]
        if parent_index == -1:
            root = child_index
        else:
            nodes[parent_index].append(child_index)
    max_height = height(nodes,root)

    return max_height + 1


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
