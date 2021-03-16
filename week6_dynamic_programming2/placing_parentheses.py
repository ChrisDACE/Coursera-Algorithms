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


def min_n_max(mins, maxs, ops, i, j):
    Min = float('inf')
    Max = float('-inf')
    for k in range(i, j):
        a = evalt(mins[i][k], mins[k + 1][j], ops[k])
        b = evalt(mins[i][k], maxs[k + 1][j], ops[k])
        c = evalt(maxs[i][k], mins[k + 1][j], ops[k])
        d = evalt(maxs[i][k], maxs[k + 1][j], ops[k])
        opts_1 = [a, b, c, d, Min]
        opts_2 = [a, b, c, d, Max]
        Min = min(opts_1)
        Max = max(opts_2)
    return Min, Max


def get_maximum_value(dataset):
    # write your code here
    length = int((len(dataset) + 1) / 2)
    nums = [int(dataset[2 * i]) for i in range(length)]
    ops = [dataset[2 * j + 1] for j in range(length - 1)]

    dp_max = [[0] * length for k in range(length)]
    dp_min = [[0] * length for k in range(length)]
    for i in range(length):
        dp_max[i][i] = nums[i]
        dp_min[i][i] = nums[i]

    for s in range(length):
        for i in range(length - s -1):
            j = i + s+1
            dp_min[i][j], dp_max[i][j] = min_n_max(dp_min, dp_max, ops, i, j)

    return dp_max[0][-1]


if __name__ == "__main__":
    # exp = '5-8+7*4-8+9'
    # print(get_maximum_value(exp))
    print(get_maximum_value(input()))
