# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points_greedy(segments):
    """You are responsible for collecting signatures from all tenants of a certain build- ing. 
    For each tenant, you know a period of time when he or she is at home. You would like to 
    collect all signatures by visiting the building as few times as possible. The mathematical model 
    for this problem is the following: You are given a set of segments on a line and your goal is to 
    mark as few points on a line as possible so that each segment contains at least one marked point.

    Task 
    Given a set of 𝑛 segments {[𝑎0,𝑏0],[𝑎1,𝑏1],...,[𝑎𝑛−1,𝑏𝑛−1]} with integer coordinates on a line, find 
    the minimum number 𝑚 of points such that each segment contains at least one point. That is, find 
    a set of integers 𝑋 of the minimum size such that for any segment [𝑎𝑖,𝑏𝑖] there is a point 𝑥 ∈ 𝑋 
    such that 𝑎𝑖 ≤ 𝑥 ≤ 𝑏𝑖.

    Input Format 
    The first line of the input contains the number 𝑛 of segments. Each of the following 𝑛 lines contains 
    two integers 𝑎𝑖 and 𝑏𝑖 (separated by a space) defining the coordinates of endpoints of the 𝑖-th segment.

    Constraints
    1 ≤ 𝑛 ≤ 100
    0 ≤ 𝑎𝑖 ≤ 𝑏𝑖 ≤ 10^9 for all 0 ≤ 𝑖 < 𝑛.

    Output Format 
    Output the minimum number 𝑚 of points on the first line and the integer coordinates of 𝑚 points 
    (separated by spaces) on the second line. You can output the points in any order. If there are many 
    such sets of points, you can output any set. (It is not difficult to see that there always exist a 
    set of points of the minimum size such that all the coordinates of the points are integers.)"""

    # safe move: place a point on the end of left-most segment or vice versa
    # sort segments by end point (left-most = index 0, right-most = index -1)
    segments = sorted(segments, key=lambda x: x[1])
    points = []

    while segments:
        # terminate when all segments covered
        safe_point = segments[0].end  # execute safe move
        points.append(safe_point)
        segments = [s for s in segments if safe_point <
                    s.start or safe_point > s.end]

    return points


def optimal_points_wrong(segments):

    points = []
    points_dict = {}

    min_point = 10e9
    max_point = 0

    for s in segments:
        points.append(s.start)
        points.append(s.end)

    for p in set(points):
        for s in segments:
            if p >= s.start and p <= s.end:
                try:
                    points_dict[p].append(segments.index(s))
                except KeyError:
                    points_dict.update({p: [segments.index(s)]})

    res = []

    while points_dict:

        points_dict = {k: v for k, v in sorted(
            points_dict.items(), key=lambda item: len(item[1]))}

        res.append(list(points_dict.keys())[-1])
        to_remove = list(points_dict.values())[-1]
        points_dict.pop(list(points_dict.keys())[-1])

        if not points_dict:
            return res

        for k, v in points_dict.items():
            for i in to_remove:
                if i in v:
                    v.remove(i)

        for k, v in points_dict.copy().items():
            if not points_dict[k]:
                points_dict.pop(k)

    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(
        x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points_greedy(segments)
    print(len(points))
    print(*points)
