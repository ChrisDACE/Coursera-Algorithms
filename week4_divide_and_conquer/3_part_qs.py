# Uses python3
import sys
import random


def partition3(a, l, r):
    # write your code here
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    for id in range(j+1,r+1):
        if a[id]==x:
            a.insert(j,a.pop(id))

    indices = [i for i in range(l, r + 1) if a[i] == x]
    m1, m2 = indices[0], indices[-1]
    return m1, m2


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)


    a[l], a[k] = a[k], a[l]
    # use partition 2
    # m = partition2(a, l, r)
    # randomized_quick_sort(a, l, m - 1);
    # randomized_quick_sort(a, m + 1, r);

    # use partition 3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # a=[2,2,2,2,1,1,1]
    # n=len(a)
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
