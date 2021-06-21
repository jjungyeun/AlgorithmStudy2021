houseCnt = 0
villageNum = []


def goNext(r, c, t):
    if t == 0:
        return r + 1, c
    elif t == 1:
        return r - 1, c
    elif t == 2:
        return r, c + 1
    elif t == 3:
        return r, c - 1


def dfs(hereR, hereC):
    global N, board, isVisited, houseCnt

    # 단지 내 집 수 증가
    houseCnt += 1

    # 현재 칸에서 상하좌우로 움직였을 때
    for t in range(4):
        thereR, thereC = goNext(hereR, hereC, t)
        # 범위안에 들어갈 때
        if 0 <= thereR < N and 0 <= thereC < N:
            # 집이 있는 위치이며, 방문한 적 없으면 방문
            if board[thereR][thereC] == 1 and isVisited[thereR][thereC] == 0:
                isVisited[thereR][thereC] = 1
                dfs(thereR, thereC)


def getVillages():
    global N, houseCnt, villageNum, board, isVisited

    # 방문한적 없는 집 찾고, 그 집과 인접한 집들 방문하면서 개수 세기
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1 and isVisited[r][c] == 0:
                houseCnt = 0
                isVisited[r][c] = 1
                dfs(r, c)
                villageNum.append(houseCnt)

    print(len(villageNum))
    villageNum.sort()
    for v in villageNum:
        print(v)


if __name__ == '__main__':
    N = int(input())
    board = [[0] * N for _ in range(N)]
    isVisited = [[0] * N for _ in range(N)]
    for i in range(N):
        tmp = input()
        for j in range(N):
            board[i][j] = int(tmp[j])

    getVillages()