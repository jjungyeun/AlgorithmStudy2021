import sys
from collections import deque


def goNext(r, c, d):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    return r + dr[d], c + dc[d]


def findLand(r, c, islandNum):
    global N, board

    queue = deque()
    queue.append((r, c))
    board[r][c] = islandNum

    while len(queue) > 0:
        hereR, hereC = queue.popleft()

        isCoast = False
        for d in range(4):
            nextR, nextC = goNext(hereR, hereC, d)
            if 0 <= nextR < N and 0 <= nextC < N:
                if board[nextR][nextC] == 1:
                    board[nextR][nextC] = islandNum
                    queue.append((nextR, nextC))
                elif board[nextR][nextC] == 0:
                    isCoast = True

        if not isCoast:
            board[hereR][hereC] = -1


def getIslandNums():
    global N, board

    islandCnt = 1   # 2 이상의 자연수
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                islandCnt += 1
                findLand(r, c, islandCnt)


def getBridge(startR, startC, startIsland):
    global N, board, shortest
    queue = deque()
    visited = [[0] * N for _ in range(N)]
    queue.append((startR, startC, 0))
    visited[startR][startC] = 1
    res = float('inf')

    while len(queue) > 0:
        hereR, hereC, hereCnt = queue.popleft()

        # 지금까지의 최소 다리 길이보다 길어지면 탐색 종료
        if hereCnt >= shortest:
            return res

        for d in range(4):
            nextR, nextC = goNext(hereR, hereC, d)

            # 방문한 적 없으면
            if 0 <= nextR < N and 0 <= nextC < N and visited[nextR][nextC] == 0:
                # 바다에 도착하면 queue에 삽입
                if board[nextR][nextC] == 0:
                    visited[nextR][nextC] = 1
                    queue.append((nextR, nextC, hereCnt + 1))
                elif board[nextR][nextC] != -1 and board[nextR][nextC] != startIsland:
                    return hereCnt

    return res


def getShortestBridge():
    global N, board, shortest

    getIslandNums()

    for r in range(N):
        for c in range(N):
            if board[r][c] > 1:
                bridge = getBridge(r, c, board[r][c])
                shortest = min(shortest, bridge)

    print(shortest)


if __name__ == '__main__':
    N = int(input())
    board = []
    shortest = float('inf')
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))

    getShortestBridge()