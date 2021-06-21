from queue import PriorityQueue

def goNext(r, c, d):
    if d == 0:
        return r - 1, c
    elif d == 1:
        return r + 1, c
    elif d == 2:
        return r, c - 1
    elif d == 3:
        return r, c + 1


def findMinMirror():
    global W, H, laser, board
    isVisited = [[float('inf')] * W for _ in range(H)]
    pq = PriorityQueue()
    startRow, startCol = laser[0]
    destRow, destCol = laser[1]
    isVisited[startRow][startCol] = 0
    pq.put((0, startRow, startCol, -1)) # corner, row, col, direction

    while not pq.empty():
        hereCorner, hereRow, hereCol, hereDirection = pq.get()
        # print("here: %d, (%d, %d), %d" % (hereCorner, hereRow, hereCol, hereDirection))

        if hereRow == destRow and hereCol == destCol:
            continue

        if isVisited[hereRow][hereCol] < hereCorner:
            continue

        for d in range(4):
            thereRow, thereCol = goNext(hereRow, hereCol, d)

            thereCorner = hereCorner
            if hereDirection != -1 and d != hereDirection:
                thereCorner += 1

            # print("there: %d, (%d, %d), %d" % ( thereCorner, thereRow, thereCol, d))

            # 범위를 벗어나지 않으면서, 벽이 아니고, 더 가깝게 방문할 수 있다면 큐에 넣기
            if 0 <= thereRow < H and 0 <= thereCol < W and board[thereRow][thereCol] != '*':
                isVisit = isVisited[thereRow][thereCol]
                # print("방문 가능?", isVisit)
                if isVisit >= thereCorner:
                    # print("가능!")
                    isVisited[thereRow][thereCol] = thereCorner
                    pq.put((thereCorner, thereRow, thereCol, d))

    return isVisited[destRow][destCol]


if __name__ == '__main__':
    W, H = map(int, input().split())
    board = [[0] * W for _ in range(H)]
    laser = []
    for r in range(H):
        tmp = input()
        for c in range(W):
            board[r][c] = tmp[c]
            if tmp[c] == 'C':
                laser.append((r,c))

    res = findMinMirror()
    print(res)