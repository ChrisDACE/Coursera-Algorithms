import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    last_stop = -1
    curr_stop = last_stop
    curr_dist = 0
    count = 0
    num_stops = len(stops)
    if len(stops)==0:
        if distance<=tank:
            return 0
        else:
            return -1
    if distance <= tank:
        return 0
    while curr_stop < num_stops:
        while True:
            if curr_stop + 1 < num_stops and stops[curr_stop + 1] - curr_dist <= tank:
                curr_stop += 1
            else:
                break
        if last_stop == curr_stop:
            return -1
        else:
            last_stop = curr_stop
            curr_dist = stops[curr_stop]
            count += 1
            if distance - stops[curr_stop] <= tank:
                return count


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
