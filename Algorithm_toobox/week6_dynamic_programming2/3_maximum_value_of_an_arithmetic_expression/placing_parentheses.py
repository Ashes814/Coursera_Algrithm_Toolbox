# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def min_and_max(i, j, op,m,M):
    minu = +float('inf')
    maxi = -float('inf')

    for k in range(i, j):
        a = evalt(M[i][k], M[k+1][j],op[k])
        b = evalt(M[i][k], m[k+1][j],op[k])
        c = evalt(m[i][k], M[k+1][j],op[k])
        d = evalt(m[i][k], m[k+1][j],op[k])
        minu = min(minu,a,b,c,d)
        maxi = max(maxi,a,b,c,d)

    return minu, maxi


def get_maximum_value(dataset):
    #write your code here
    d = dataset[0::2]
    op = dataset[1:-1:2]
    n = len(d)
    m = [[0 for i in range(n)] for j in range(n)]
    M = [[0 for i in range(n)] for j in range(n)]
    for i in range(0, n):
        m[i][i] = int(d[i])
        M[i][i] = int(d[i])

    for s in range(1,n):
        for i in range(0, n-s):
            j = i+s
            m[i][j], M[i][j] = min_and_max(i,j,op,m,M)

    return M[0][n-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))

# print(get_maximum_value('5-8+7*4-8+9'))
#
# print(get_maximum_value('1+6'))