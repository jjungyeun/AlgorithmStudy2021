from collections import deque

isVisited = [0] * 1000001


def bfs(N, M):
    global isVisited
    res = -1
    queue = deque()

    queue.append((0, N)) # (cnt, n)
    while len(queue) > 0:
        hereCnt, hereNum = queue.popleft()

        if hereNum == M:
            res = hereCnt
            break

        if hereNum > 1000000 or hereNum < 1:
            continue

        # print(hereCnt, hereNum)
        if isVisited[hereNum]:
            # print("이미 방문")
            continue

        isVisited[hereNum] = 1
        queue.append((hereCnt+1, hereNum+1))
        queue.append((hereCnt+1, hereNum-1))
        queue.append((hereCnt+1, hereNum*2))
        queue.append((hereCnt+1, hereNum-10))

    return res


if __name__ == '__main__':
    TC = int(input())
    for T in range(1, TC + 1):
        N, M = map(int, input().split())
        isVisited = [0] * 1000001
        res = bfs(N, M)
        print("#%d %d" % (T, res))
