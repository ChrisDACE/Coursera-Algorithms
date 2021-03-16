# Uses python3

def edit_distance(s, t):
    # write your code here
    dists = [[0] * (len(t) + 1) for i in range(len(s) + 1)]
    for i in range(len(s) + 1):
        for j in range(len(t) + 1):
            if i == 0:
                dists[i][j] = j
            elif j == 0:
                dists[i][j] = i
            elif s[i - 1] == t[j - 1]:
                dists[i][j] = dists[i - 1][j - 1]
            else:
                dists[i][j] = 1 + min(dists[i - 1][j],
                                      dists[i][j - 1],
                                      dists[i - 1][j - 1])

    return dists[-1][-1]


if __name__ == "__main__":
    # print(edit_distance(input(), input()))
    str1 = '1'
    str2 = '1234'
    print(edit_distance(str1, str2))
