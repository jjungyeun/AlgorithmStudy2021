import sys
from collections import deque


def goNext(r, c, d):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    return r + dr[d], c + dc[d]


def bfs():
    global H, W, board, visited
    queue = deque()
    queue.append((0, 0, 1, 0)) # r, c, dist, canBreak

    while len(queue)>0:
        hereR, hereC, hereDist, canBreak = queue.popleft()

        if hereR == H - 1 and hereC == W - 1:
            return hereDist

        for d in range(4):
            nextR, nextC = goNext(hereR, hereC, d)
            if 0 <= nextR < H and 0 <= nextC < W and visited[nextR][nextC][canBreak] == 0:
                # 빈 공간 (그냥 이동 가능)
                if board[nextR][nextC] == '0':
                    visited[nextR][nextC][canBreak] = 1
                    queue.append((nextR, nextC, hereDist + 1, canBreak))

                # 벽 있는 공간 (벽 부수고 이동 가능)
                if canBreak == 0 and board[nextR][nextC] == '1':
                    visited[nextR][nextC][canBreak] = 1
                    queue.append((nextR, nextC, hereDist + 1, 1))

    return -1


if __name__ == '__main__':
    H, W = map(int, input().split())
    board = [0] * H
    visited = [[[0, 0] for _ in range(W)] for _ in range(H)]
    for i in range(H):
        board[i] = [*sys.stdin.readline().strip()]

    print(bfs())