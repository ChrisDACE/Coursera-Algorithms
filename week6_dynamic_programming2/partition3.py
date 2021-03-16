# Uses python3
import sys
import itertools
from collections import Counter


def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0


def partition3_dp(A):
    sums = int(sum(A) / 3)
    results = [[0] * (len(A) + 1) for i in range(sums + 1)]

    for j in range(len(A) + 1):
        results[0][j] = 1
    for i in range(1, sums + 1):
        for j in range(1, len(A) + 1):
            results[i][j] = results[i][j - 1]
            if A[j - 1] <= i:
                results[i][j] = (results[i - A[j - 1]][j - 1] or results[i][j - 1])

    if Counter(results[-1])[1] >= 3:
        return 1
    else:
        return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    # A = [17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]
    if sum(A) % 3 != 0:
        print(0)
    else:
        print(partition3_dp(A))
