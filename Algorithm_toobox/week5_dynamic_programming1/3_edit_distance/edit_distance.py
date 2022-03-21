# Uses python3
def edit_distance(wordA, wordB):
    #write your code here
    n = len(wordA)
    m = len(wordB)

    D = []
    for i in range(n + 1):
        D.append([])
        for j in range(m + 1):
            D[i].append(0)
    for i in range(n + 1):
        D[i][0] = i
    for j in range(m + 1):
        D[0][j] = j

    for j in range(1, m + 1):
        for i in range(1, n + 1):
            insertion = D[i][j - 1] + 1
            deletion = D[i - 1][j] + 1
            match = D[i - 1][j - 1]
            mismatch = D[i - 1][j - 1] + 1

            if wordA[i - 1] == wordB[j - 1]:
                D[i][j] = min(insertion, deletion, match)
            else:
                D[i][j] = min(insertion, deletion, mismatch)
    return D[-1][-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))

# print(edit_distance('editing','distance'))
# print(edit_distance('ab','ab'))
# print(edit_distance('short','ports'))