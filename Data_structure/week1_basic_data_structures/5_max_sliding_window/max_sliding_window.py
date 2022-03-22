# # python3
#
# class MyQueue(object):
#     i_stack = []
#     o_stack = []
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.i_stack = []
#         self.o_stack = []
#
#     def push(self, x):
#         """
#         Push element x to the back of queue.
#         :type x: int
#         :rtype: void
#         """
#         self.i_stack.append(x)
#
#     def pop(self):
#         """
#         Removes the element from in front of queue and returns that element.
#         :rtype: int
#         """
#         self.peek()
#         return self.o_stack.pop()
#
#     def peek(self):
#         """
#         Get the front element.
#         :rtype: int
#         """
#         if len(self.o_stack) == 0:
#             i_len = len(self.i_stack)
#             for i in range(i_len):
#                 self.o_stack.append(self.i_stack.pop())
#         return self.o_stack[-1]
#
#     def empty(self):
#         """
#         Returns whether the queue is empty.
#         :rtype: bool
#         """
#         return len(self.i_stack) == 0 and len(self.o_stack) == 0
#
#
# class StackWithMax():
#     def __init__(self, stack, max_first):
#         self.stack = stack
#         self.max_stack = []
#
#
#     def Push(self, a):
#         self.stack.append(a)
#         if self.max_stack == []:
#             self.max_stack.append(a)
#         if a > self.max_stack[-1]:
#             self.max_stack.append(a)
#         else:
#             self.max_stack.append(self.max_stack[-1])
#
#     def Pop(self):
#
#         assert(len(self.stack))
#
#         self.max_stack.pop()
#         return self.stack.pop()
#
#     def Max(self):
#         assert(len(self.stack))
#         return self.max_stack[-1]

def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))
    return maximums

def max_sliding_window_efficient(sequence, m):
    n = len(sequence)
    # stack1 = StackWithMax(sequence[0:n-m-1], max(sequence[0:n-m+1]))
    # stack2 = StackWithMax([], 0)
    # stack1 = sequence[0:n-m+1]
    # stack2 = []
    from collections import deque
    my_deque = deque()
    # my_deque.extend(sequence[0:n-m])
    maximums = []
    for i in range(m):
        while my_deque and sequence[i] >= sequence[my_deque[-1]]:
            my_deque.pop()
        my_deque.append(i)
    for i in range(m, n):
        maximums.append(sequence[my_deque[0]])
        while my_deque and my_deque[0] <= i-m:
            my_deque.popleft()

        while my_deque and sequence[i] >= sequence[my_deque[-1]]:
            my_deque.pop()

        my_deque.append(i)
    maximums.append(sequence[my_deque[0]])
    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_efficient(input_sequence, window_size))
'''
8
2 7 3 1 5 2 6 2
4
'''