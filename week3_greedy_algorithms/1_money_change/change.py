# Uses python3
import sys

def get_change(m):
    #write your code here
    n = 0
    while m > 0:
        if m >= 10:
            m = m - 10
            n += 1
        elif m >= 5:
            m = m - 5
            n += 1
        elif m >= 1:
            m = m - 1
            n += 1

    return n

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))


#print(get_change(2), get_change(28), get_change(999))