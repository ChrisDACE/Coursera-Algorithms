# Uses python3

import sys


def lcs2(a, b):
    # write your code here
    m = len(a)
    n = len(b)
    length = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                length[i][j] = length[i - 1][j - 1] + 1
            else:
                length[i][j] = max(length[i - 1][j],
                                   length[i][j - 1],
                                   length[i - 1][j - 1])

    return length[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
