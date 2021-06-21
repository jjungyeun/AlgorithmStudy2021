from collections import deque


# t = 1: go 1 / 2: go 2 / 3: go 3 / 4: turn left / 5: turn right
# d = 1: right, 2: left, 3: down, 4: up
def goNext(r, c, d, t):
    left = [0, 4, 3, 1, 2]
    right = [0, 3, 4, 2, 1]
    if 1 <= t <= 3:  # go t
        if d == 1:
            return r, c + t, d
        elif d == 2:
            return r, c - t, d
        elif d == 3:
            return r + t, c, d
        elif d == 4:
            return r - t, c, d
    elif t == 4:    # turn left
        return r, c, left[d]
    elif t == 5:    # turn right
        return r, c, right[d]


def printBoard(b, robot):
    global H, W
    d = ['', 'r', 'l', 'd', 'u']
    robotR, robotC, robotD = robot

    print('-----------------')
    for i in range(H):
        for j in range(W):
            if i == robotR and j == robotC:
                print(d[robotD], end=' ')
            elif b[i][j] == 0:
                print('.', end=' ')
            else:
                print('#', end=' ')
        print()
    print('-----------------\n')


def getMinCmd():
    global H, W, board, sRow, sCol, sDir, dRow, dCol, dDir
    queue = deque()
    queue.append((sRow, sCol, sDir, 0))
    isVisited = [[[0] * 5 for _ in range(W)] for _ in range(H)]
    isVisited[sRow][sCol][sDir] = 1

    while len(queue) > 0:
        hereRow, hereCol, hereDir, hereCmd = queue.popleft()
        # print(hereRow, hereCol, hereDir, hereCmd)
        #
        # printBoard(board, (hereRow, hereCol, hereDir))

        if (hereRow, hereCol, hereDir) == (dRow, dCol, dDir):
            return hereCmd

        canGo = True    # 벽때문에 더이상 못가는지 표시하는 변수
        for t in range(1, 6):
            thereRow, thereCol, thereDir = goNext(hereRow, hereCol, hereDir, t)
            if 0 <= thereRow < H and 0 <= thereCol < W:
                # 벽이 있었으면 패스
                if 1 <= t <= 3 and canGo is False:
                    continue
                # 벽이 있으면 패스
                if board[thereRow][thereCol] == 1:
                    canGo = False
                    continue
                if board[thereRow][thereCol] == 0 and isVisited[thereRow][thereCol][thereDir] == 0:
                    isVisited[thereRow][thereCol][thereDir] = 1
                    queue.append((thereRow, thereCol, thereDir, hereCmd + 1))

    return float('inf')


if __name__ == '__main__':
    H, W = map(int, input().split())
    board = [0] * (H)
    for i in range(H):
        board[i] = list(map(int, input().split()))
    sRow, sCol, sDir = map(int, input().split())
    dRow, dCol, dDir = map(int, input().split())
    sRow -= 1
    sCol -= 1
    dRow -= 1
    dCol -= 1

    res = getMinCmd()
    print(res)