import sys


def giveBooks():
    global N, M, want, given

    cnt = 0

    for left, right in want:
        for book in range(left, right+1):
            if given[book] == 0:
                given[book] = 1
                cnt += 1
                break

    print(cnt)


if __name__ == '__main__':
    TC = int(input())
    for T in range(TC):
        N, M = map(int, input().split())
        want = [0 for _ in range(M)]
        given = [0 for _ in range(N+1)]

        for stu in range(M):
            a, b = map(int, sys.stdin.readline().split())
            want[stu] = (a, b)

        want.sort(key=lambda item: item[1])
        giveBooks()
