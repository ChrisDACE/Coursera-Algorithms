import sys


def get_optimal_value(capacity, weights, values):
    # value = 0.
    # write your code here
    dict = {}
    curr_w = 0
    v_all = 0
    for i in range(len(values)):
        dict[values[i]] = weights[i]
    dict = sorted(dict.items(), key=lambda k: k[0] / k[1], reverse=True)
    for item in dict:
        v = int(item[0])
        w = int(item[1])
        if curr_w + w >= capacity:
            v_all += v * (capacity - curr_w) / w
            break
        else:
            v_all += v
            curr_w += w
    return v_all


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
