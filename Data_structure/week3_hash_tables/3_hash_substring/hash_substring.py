# # python3
# import time
# # def read_input():
# #     return (input().rstrip(), input().rstrip())
# #
# # def print_occurrences(output):
# #     print(' '.join(map(str, output)))
# #
# def get_occurrences(pattern, text):
#     return [
#         str(i)
#         for i in range(len(text) - len(pattern) + 1)
#         if text[i:i + len(pattern)] == pattern
#     ]
#
#
# def PolyHash(string, prime, multiplier):
#     hash_value = 0
#     for i in range(len(string) - 1, -1, -1):
#         hash_value = (hash_value * multiplier + ord(string[i])) % prime
#     return hash_value
#
#
# def PrecomputedHashes(text, pattern, prime, multiplier):
#     t = len(text)
#     p = len(pattern)
#     s = text[t - p:]
#     H = list([] for _ in range(t - p + 1))
#     H[t - p] = PolyHash(s, prime, multiplier)
#     y = 1
#     for i in range(1, p + 1):
#         y = (y * multiplier) % prime
#     for i in range(t - p - 1, -1, -1):
#         H[i] = (multiplier * H[i + 1] + ord(text[i]) - y * ord(text[i + p])) % prime
#     return H
#
#
# # def RabinKarp(pattern, text):
#     # result = []
#     # phash = hash(pattern)
#     #
#     #
#     # for i in range(0, len(text) - len(pattern) + 1):
#     #     thash = hash(text[i:i + len(pattern)])
#     #     if phash != thash:
#     #         continue
#     #     if text[i:i + len(pattern)] == pattern:
#     #         result.append(i)
#     # return result
#
# def RabinKarp(pattern, text):
#     t = len(text)
#     p = len(pattern)
#     prime = 1000000007
#     multiplier = 236
#     result = []
#     pattern_hash = PolyHash(pattern, prime, multiplier)
#     hash_substrings = PrecomputedHashes(text, pattern, prime, multiplier)
#     for i in range(t - p + 1):
#         if pattern_hash == hash_substrings[i]:
#             result.append(i)
#     return
#
# if __name__ == '__main__':
#
#     with open('tests/06', 'r') as file:
#         strings = file.read().rsplit()
#         p_string = strings[0]
#         t_string = strings[1]
#         file.close()
#     with open('tests/06.a', 'r') as file:
#         answer = file.read().strip().split()
#         file.close()
#
#     naive_start = time.time()
#     answer1 = get_occurrences(p_string, t_string)
#     answer2 = get_occurrences('abc', 'abacaba')
#     answer3 = get_occurrences('Test', 'testTesttesT')
#     answer4 = get_occurrences('aaaaa', 'baaaaaaa')
#     naive_end = time.time()
#     naive_time = naive_end - naive_start
#
#     rk_t0 = time.time()
#     RabinKarp_result1 = RabinKarp(p_string, t_string)
#     RabinKarp_result2 = RabinKarp('abc', 'abacaba')
#     RabinKarp_result3 = RabinKarp('Test', 'testTesttesT')
#     RabinKarp_result4 = RabinKarp('aaaaa', 'baaaaaaa')
#     rk_time = time.time() - rk_t0
#     print(answer1, RabinKarp_result1)
#     print(answer2, RabinKarp_result2)
#     print(answer3, RabinKarp_result3)
#     print(answer4, RabinKarp_result4)
#
#     print('naive:time: ',naive_time, 'RabinKarp:time: ',rk_time)
def PolyHash(string, prime, multiplier):
    hash_value = 0
    for i in range(len(string) - 1, -1, -1):
        hash_value = (hash_value * multiplier + ord(string[i])) % prime
    return hash_value


def PrecomputedHashes(text, pattern, prime, multiplier):
    t = len(text)
    p = len(pattern)
    s = text[t - p:]
    H = list([] for _ in range(t - p + 1))
    H[t - p] = PolyHash(s, prime, multiplier)
    y = 1
    for i in range(1, p + 1):
        y = (y * multiplier) % prime
    for i in range(t - p - 1, -1, -1):
        H[i] = (multiplier * H[i + 1] + ord(text[i]) - y * ord(text[i + p])) % prime
    return H


def RabinKarp(text, pattern):
    t = len(text)
    p = len(pattern)
    prime = 1000000007
    multiplier = 236
    result = []
    pattern_hash = PolyHash(pattern, prime, multiplier)
    hash_substrings = PrecomputedHashes(text, pattern, prime, multiplier)
    for i in range(t - p + 1):
        if pattern_hash == hash_substrings[i]:
            result.append(i)
    return result


if __name__ == '__main__':
    pattern = input()
    text = input()
    positions = RabinKarp(text, pattern)
    for pos in positions:
        print(pos, end=' ')