# Uses python3
import sys


def get_change(m):
    # write your code here
    min_num = -1
    coins = [1, 3, 4]
    nums = [0]

    for i in range(1, m + 1):
        curr_num = []
        for j in range(len(coins)):
            if i >= coins[j]:
                temp_num = nums[i - coins[j]] + 1
                curr_num.append(temp_num)
        nums.append(min(curr_num))

    return nums[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
