# python3

# class Query:
#
#     def __init__(self, query):
#         self.type = query[0]
#         if self.type == 'check':
#             self.ind = int(query[1])
#         else:
#             self.s = query[1]


# class QueryProcessor:
#     _multiplier = 263
#     _prime = 1000000007
#
#     def __init__(self, bucket_count):
#         self.bucket_count = bucket_count
#         # store all strings in one list
#         self.elems = []
#
#     def _hash_func(self, s):
#         ans = 0
#         for c in reversed(s):
#             ans = (ans * self._multiplier + ord(c)) % self._prime
#         return ans % self.bucket_count
#
#     def write_search_result(self, was_found):
#         print('yes' if was_found else 'no')
#
#     def write_chain(self, chain):
#         print(' '.join(chain))
#
#     def read_query(self):
#         return Query(['add', 'world'])
#
#     def process_query(self, query):
#         if query.type == "check":
#             # use reverse order, because we append strings to the end
#             self.write_chain(cur for cur in reversed(self.elems)
#                         if self._hash_func(cur) == query.ind)
#         else:
#             try:
#                 ind = self.elems.index(query.s)
#             except ValueError:
#                 ind = -1
#             if query.type == 'find':
#                 self.write_search_result(ind != -1)
#             elif query.type == 'add':
#                 if ind == -1:
#                     self.elems.append(query.s)
#             else:
#                 if ind != -1:
#                     self.elems.pop(ind)

# def process_queries(self):
#     # n = int(input())
#     n = 12
#     for i in range(n):
#         self.process_query(self.read_query())
def hash_func(s, bucket_count):
    multiplier = 263
    prime = 1000000007
    ans = 0
    for c in reversed(s):
        ans = (ans * multiplier + ord(c)) % prime
    return ans % bucket_count


if __name__ == '__main__':
    bucket_count = int(input())
    input_lines = int(input())
    input_list = []
    for n in range(input_lines):
        line = input().split(' ')
        input_list.append(line)
    # bucket_count = 5
    # input_lines = 12
    # input_list = [['add', 'world'], ['add', 'HellO'], ['check', '4'], ['find', 'World'], ['find', 'world'], ['del', 'world'], ['check', '4'], ['del', 'HellO'], ['add', 'luck'], ['add', 'GooD'], ['check', '2'], ['del', 'good']]
    # bucket_count = 4
    # input_lines = 8
    # input_list = [['add', 'test'], ['add', 'test'], ['find', 'test'], ['del', 'test'], ['find', 'test'], ['find', 'Test'], ['add', 'Test'], ['find', 'Test']]
    hash_table = {}
    in_table = []
    for line in input_list:
        if line[0] == 'add':
            hash_value = hash_func(line[1], bucket_count)
            if hash_value not in hash_table.keys():
                hash_table[hash_value] = []
                hash_table[hash_value].append(line[1])
                in_table.append(line[1])
            else:
                if line[1] in hash_table[hash_value]:
                    pass
                else:
                    hash_table[hash_value].append(line[1])
                    in_table.append(line[1])
        if line[0] == 'check':
            hash_value = int(line[1])
            if hash_value not in hash_table.keys():
                print('')
            else:
                print(' '.join(str(word) for word in hash_table[hash_value][::-1]))

        if line[0] == 'find':
            if line[1] in in_table:
                print('yes')
            else:
                print('no')
        if line[0] == 'del':
            hash_value = hash_func(line[1], bucket_count)
            if hash_value not in hash_table.keys():
                pass
            else:
                if line[1] in hash_table[hash_value]:
                    hash_table[hash_value].remove(line[1])
                    in_table.remove(line[1])
                else:
                    pass

