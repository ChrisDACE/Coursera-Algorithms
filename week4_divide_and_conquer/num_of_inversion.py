# Uses python3
import sys


def merge_part(B, C):
    i, j = 0, 0
    D = []
    num = 0
    while i < len(B) and j < len(C):
        if B[i] > C[j]:
            D.append(C[j])
            num += len(B) - i
            j += 1
        else:
            D.append(B[i])
            i += 1
    D += B[i:]
    D += C[j:]
    return num, D


def get_number_of_inversions(a):
    if len(a)==1:
        return 0, a
    else:
        B = a[:len(a)//2]
        C = a[len(a)//2:]

    num1, B = get_number_of_inversions(B)
    num2, C = get_number_of_inversions(C)
    num3, D = merge_part(B, C)

    num = num1+num2+num3
    return num, D


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # a = [9,8,7,3,2,1]
    num,sorted_a=get_number_of_inversions(a)
    print(num)
