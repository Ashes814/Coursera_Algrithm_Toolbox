# Uses python3
import sys
from collections import namedtuple
# import os

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    # points = []
    # #write your code here
    # for s in segments:
    #     points.append(s.start)
    #     points.append(s.end)
    # return points
    n = len(segments)
    points = []
    currentLine = 0
    sorted_segments = sorted(segments, key=(lambda x: [x[1], x[0]]))
    m = 0

    while currentLine < n:
        points.append(sorted_segments[currentLine][1])
        currentLine += 1
        while currentLine < n:
            if sorted_segments[currentLine][0] <= points[m] <= sorted_segments[currentLine][1]:
                currentLine += 1
            else:
                break

        m += 1


    return points


#
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)


# print(optimal_points([[1,3],[2,5],[3,6]]))
#
# print(optimal_points([[4,7],[1,3],[2,5],[5,6]]))
#
# os.system('python3 model.py <input.txt >model.txt')
# with open('input.txt', 'r', encoding = 'utf-8') as f:
#     input = f.read()
#     n, *data = map(int, input.split())
#     segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
#     points = optimal_points(segments)
#     print(len(points))
#     print(*points)