# Uses python3
import sys


def optimal_weight(W, w):
    # write your code here
    result = 0
    num = len(w)
    results = [[0] * (W + 1) for i in range(num + 1)]
    for id in range(1, num+1):
        for w_id in range(1, W+1):
            results[id][w_id]=results[id-1][w_id]
            if w[id-1] <= w_id:
                w_temp = results[id-1][w_id-w[id-1]]+w[id-1]
                if w_temp>results[id][w_id]:
                    results[id][w_id] = w_temp

    return results[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    # W=10
    # w=[1,4,8]
    print(optimal_weight(W, w))
