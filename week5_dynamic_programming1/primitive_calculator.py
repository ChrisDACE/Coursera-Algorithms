# Uses python3
import sys


def optimal_seq_dp(n):
    step_dict = {1: [1, 0]}
    for curr in range(2, n + 1):
        options = []
        if curr % 3 == 0:
            options.append(int(curr / 3))
        if curr % 2 == 0:
            options.append(int(curr / 2))
        options.append(curr - 1)

        steps = []
        for i in range(len(options)):
            steps.append(step_dict[options[i]][1])
        prev = options[steps.index(min(steps))]

        prev_v = [prev, step_dict[prev][1] + 1]
        step_dict[curr] = prev_v

    seq = [n]
    while n > 1:
        seq.append(step_dict[n][0])
        n = step_dict[n][0]
    return reversed(seq)


def optimal_sequence(n):
    """This greedy method is actually wrong!"""
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


input = sys.stdin.read()
n = int(input)
# sequence = list(optimal_sequence(n))
sequence = list(optimal_seq_dp(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
