import sys


def get_min_tapes():
    global N, L, points

    cnt, now = 0, -1

    for point in points:
        if point > now:
            now = point + L -1
            cnt += 1

    return cnt


if __name__ == '__main__':
    N, L = map(int, input().split())
    points = sorted(list(map(int, sys.stdin.readline().split())))
    print(get_min_tapes())