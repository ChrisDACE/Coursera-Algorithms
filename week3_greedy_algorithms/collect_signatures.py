# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []

    segments = sorted(segments, key=lambda tup: tup[0])
    if len(segments) == 1:
        points.append(segments[0][1])
        return points
    i = 1
    # start = 0
    min_right = segments[0][1]
    while True:
        # print(segments[start][1],i)
        while i < len(segments) and segments[i][0] <= min_right:
            min_right = min(min_right, segments[i][1])
            i += 1
        points.append(min_right)
        # print(points[-1],i)
        if i == len(segments):
            break
        min_right = segments[i][1]
        # start = i

    #
    # for s in segments:
    #     points.append(s.start)
    #     points.append(s.end)
    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    # segments=[[52,52],[55,56],[57,59],[57,58],[58,58],[58,59],[54,56],[58,58],[57,59],[52,54],[54,54]]
    # points = optimal_points(segments)
    print(len(points))
    print(*points)
