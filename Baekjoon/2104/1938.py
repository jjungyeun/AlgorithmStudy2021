from collections import deque


# 통나무가 있는 3개의 점 중에서 가운데 점을 찾는 함수
def getCenter(p1, p2, p3):
    arr = [p1, p2, p3]
    arr.sort()

    if p1[0] == p2[0]:  # 가로
        return arr[1][0], arr[1][1], 0
    else:   # 세로
        return arr[1][0], arr[1][1], 1


# 통나무의 중심좌표와 방향이 주어졌을 때, 지도 내에 있는지 체크하는 함수
def checkInBoard(cRow, cCol, d):
    global N
    if cRow < 0 or cRow >= N or cCol < 0 or cCol >= N:
        return False

    if d == 0 and (cCol == 0 or cCol == N-1):
        return False

    if d == 1 and (cRow == 0 or cRow == N-1):
        return False

    return True


# 이 위치에서 회전가능한지 판단하는 함수
def canTurn(r, c):
    global board, N

    if r == 0 or r == N-1 or c == 0 or c == N-1:
        return False

    # 중심 기준 9칸에 1이 있는지 확인
    for i in range(-1, 2):
        for j in range(-1, 2):
            nextR = r + i
            nextC = c + j
            if board[nextR][nextC] == 1:
                return False

    return True


def goNext(r, c, d, t):
    dirFunc = [1, 0]
    if t == 0:
        return r - 1, c, d
    elif t == 1:
        return r + 1, c, d
    elif t == 2:
        return r, c - 1, d
    elif t == 3:
        return r, c + 1, d
    elif t == 4:
        return r, c, dirFunc[d]


def canMove(r, c, d, t):
    global board

    # 움직이 곳이 범위 밖이거나, 회전할 수 없었던 경우 False 반환
    if not checkInBoard(r, c, d):
        return False
    if t == 4 and not canTurn(r, c):
        return False

    # 움직인 위치에 나무가 있으면(1이면) False 반환
    points = [(r, c)]
    if d == 0:
        points.append((r, c-1))
        points.append((r, c+1))
    elif d == 1:
        points.append((r-1, c))
        points.append((r+1, c))

    for p in points:
        py, px = p
        if board[py][px] == 1:
            return False

    return True


def printBoard(r, c, d):
    global N, board
    bPoint = [(r, c)]
    if d == 0:
        bPoint.append((r, c-1))
        bPoint.append((r, c+1))
    elif d == 1:
        bPoint.append((r-1, c))
        bPoint.append((r+1, c))

    print("\n-------------")
    for i in range(N):
        for j in range(N):
            if (i, j) in bPoint:
                print('B', end=' ')
            else:
                print(board[i][j], end=' ')
        print()
    print("-------------")


def getMinMove():
    global N, board, sPoint, dPoint

    sRow, sCol, sDir = getCenter(sPoint[0], sPoint[1], sPoint[2])
    dRow, dCol, dDir = getCenter(dPoint[0], dPoint[1], dPoint[2])

    queue = deque()
    isVisited = [[[0] * 2 for _ in range(N)] for _ in range(N)] # isVisited[centerRow][centerCol][가로/세로] = 0 or 1

    queue.append((sRow, sCol, sDir, 0)) # (통나무 중심 row, 통나무 중심 col, 통나무 방향(가로/세로), 현재까지의 move)
    isVisited[sRow][sCol][sDir] = 1

    while len(queue) > 0:
        hereRow, hereCol, hereDir, hereMove = queue.popleft()

        # 도착하면 종료
        if hereRow == dRow and hereCol == dCol and hereDir == dDir:
            return hereMove

        # printBoard(hereRow, hereCol, hereDir)

        for t in range(5):
            thereRow, thereCol, thereDir = goNext(hereRow, hereCol, hereDir, t)
            # 다음 좌표로 움직일 수 있고, 방문한적 없으면 방문
            if canMove(thereRow, thereCol, thereDir, t) and isVisited[thereRow][thereCol][thereDir] == 0:
                isVisited[thereRow][thereCol][thereDir] = 1
                queue.append((thereRow, thereCol, thereDir, hereMove + 1))

    return 0


if __name__ == '__main__':
    N = int(input())
    board = [[0]* N for _ in range(N)]
    sPoint = []
    dPoint = []

    for i in range(N):
        tmp = input()
        for j in range(N):
            if tmp[j] == 'B':
                sPoint.append((i, j))
            elif tmp[j] == 'E':
                dPoint.append((i, j))
            elif tmp[j] == '1':
                board[i][j] = int(tmp[j])

    res = getMinMove()
    print(res)
