from collections import deque
import sys

dr, dc = [1,-1,0,0], [0,0,1,-1]


def spreadFire():
    global fireList, board
    tmp = []

    for fireR, fireC in fireList:

        for d in range(4):
            nextR, nextC = fireR + dr[d], fireC + dc[d]

            # 불이 번질 수 있는 칸이라면, 다음 차례때 이 칸에서부터 불이 다시 번질 수 있도록 저장
            if 0 <= nextR < R and 0 <= nextC < C and board[nextR][nextC] == '.':
                board[nextR][nextC] = 'F'
                tmp.append((nextR, nextC))

    fireList = tmp


def escapeMaze():
    global R, C, board, visited, start

    queue = deque()
    queue.append((start[0], start[1], 0))
    visited[start[0]][start[1]] = 1

    fireCnt = 0

    while len(queue) > 0:
        hereR, hereC, hereCnt = queue.popleft()

        if fireCnt != hereCnt:
            spreadFire()
            fireCnt += 1

        if board[hereR][hereC] == 'F':
            continue

        for d in range(4):
            nextR, nextC, nextCnt = hereR + dr[d], hereC + dc[d], hereCnt + 1

            if 0 <= nextR < R and 0 <= nextC < C:
                # 처음 방문했으며 방문 가능한 곳이라면 방문
                if visited[nextR][nextC] == 0 and board[nextR][nextC] == '.':
                    visited[nextR][nextC] = 1
                    queue.append((nextR, nextC, nextCnt))

            # 탈출 성공
            else:
                return nextCnt

    return "IMPOSSIBLE"


if __name__ == '__main__':
    R, C = map(int, input().split())
    board = []
    visited = [[0 for _ in range(C)] for _ in range(R)]
    fireList = []

    for r in range(R):
        tmp = [*sys.stdin.readline().strip()]
        for c in range(C):
            if tmp[c] == 'J':
                start = (r, c)
                tmp[c] = '.'
            elif tmp[c] == 'F':
                fireList.append((r, c))
        board.append(tmp)

    print(escapeMaze())