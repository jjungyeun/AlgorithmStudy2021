import sys


def getMinSum():
    global K, sensors

    diffs = sorted([sensors[i]-sensors[i-1] for i in range(1, len(sensors))], reverse=True)

    res = 0
    for diff in diffs[K-1:]:
        res += diff

    return res


if __name__ == '__main__':
    N = int(input())
    K = int(input())
    sensors = sorted(set(map(int, sys.stdin.readline().split())))

    print(getMinSum())
