from collections import deque
from copy import deepcopy


def goNext(r, c, t):
    if t == 0:
        return r + 1, c
    if t == 1:
        return r, c + 1
    if t == 2:
        return r - 1, c
    if t == 3:
        return r, c - 1


def spreadVirus(lab):
    board = deepcopy(lab)
    global N, M, virusPoint, emptyCells, maxSafetyArea
    restSA = emptyCells - 3

    # 큐 생성 및 바이러스 있는 위치 넣기
    queue = deque()
    for p in virusPoint:
        queue.append(p)

    while len(queue) > 0:
        hereRow, hereCol = queue.popleft()

        # 안전영역이 최대치보다 작아지면 종료
        if restSA <= maxSafetyArea:
            break

        # 상하좌우에 바이러스 퍼트리기
        for i in range(4):
            nextRow, nextCol = goNext(hereRow, hereCol, i)
            # 이동할 칸이 보드 안에 있고, 빈 공간이면 바이러스 퍼트리기
            if 0 <= nextRow < N and 0 <= nextCol < M and board[nextRow][nextCol] == 0:
                board[nextRow][nextCol] = 2
                restSA -= 1
                queue.append((nextRow, nextCol))

    # print("restSA: ", restSA)
    maxSafetyArea = max(maxSafetyArea, restSA)


def getSafetyArea():
    global N, M, lab, emptyPoint, emptyCells, maxSafetyArea

    for i in range(emptyCells-2):
        r_i, c_i = emptyPoint[i]
        lab[r_i][c_i] = 1
        for j in range(i+1, emptyCells-1):
            r_j, c_j = emptyPoint[j]
            lab[r_j][c_j] = 1
            for k in range(j+1, emptyCells):
                # print(i, j, k)
                r_k, c_k = emptyPoint[k]
                lab[r_k][c_k] = 1
                # 벽 3개 세운 상태로 바이러스 퍼트려보기
                spreadVirus(lab)

                # 새로 세운 벽으로 바이러스를 완벽히 막는 경우가 생기면 바로 종료
                if maxSafetyArea == emptyCells - 3:
                    return

                lab[r_k][c_k] = 0
            lab[r_j][c_j] = 0
        lab[r_i][c_i] = 0


if __name__ == '__main__':
    N, M = map(int, input().split())
    lab = [[0] * M for _ in range(N)]
    virusPoint = []
    emptyPoint = []
    maxSafetyArea = 0
    for i in range(N):
        tmp = list(map(int, input().split()))
        for j in range(M):
            here = tmp[j]
            if here == 2:
                virusPoint.append((i, j))
            elif here == 0:
                emptyPoint.append((i, j))
            lab[i][j] = here

    emptyCells = len(emptyPoint)
    getSafetyArea()
    print(maxSafetyArea)