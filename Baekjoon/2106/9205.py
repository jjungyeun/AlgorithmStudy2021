import sys
from collections import deque


def get_manhattan_dist(s, d):
    s_x, s_y = s
    d_x, d_y = d
    return abs(s_x-d_x) + abs(s_y-d_y)


def walk_with_drinking(T):
    global home, festival, cvs, visited

    queue = deque()
    queue.append(home)

    while len(queue) > 0:
        here = queue.popleft()
        dist = get_manhattan_dist(here, festival)

        # 현재 위치에서 축제까지 맥주 20개로 갈 수 있으면 True 반환하고 종료
        if dist <= 1000:
            return True

        # 축제까지 맥주 모자라는 경우 편의점 들리기
        for i in range(N):
            cvs_position = cvs[i]
            cvs_dist = get_manhattan_dist(here, cvs_position)
            if visited[i] != T and cvs_dist <= 1000:
                visited[i] = T
                queue.append(cvs_position)

    return False


if __name__ == '__main__':
    TC = int(input())
    cvs = []
    visited = [0 for _ in range(100)]
    home, festival = None, None

    for T in range(1, TC+1):
        N = int(input())
        home = tuple(map(int, sys.stdin.readline().split()))
        cvs.clear()
        for _ in range(N):
            cvs.append(tuple(map(int, sys.stdin.readline().split())))
        festival = tuple(map(int, sys.stdin.readline().split()))

        if walk_with_drinking(T):
            print("happy")
        else:
            print("sad")