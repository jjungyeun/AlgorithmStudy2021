from collections import deque


# d 방향으로 구슬 1과 구슬 2를 순서대로 이동시키는 함수
# 두 구슬의 이동 후 좌표를 반환 (구멍에 빠지면 (-1,-1)를 반환)
def roll(marble1, marble2, d):
    global board

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 구슬 1 먼저 이동
    preR, preC = marble1
    while True:
        hereR, hereC = preR + dr[d], preC + dc[d]
        if board[hereR][hereC] == '#':
            res1 = (preR, preC)
            break
        elif board[hereR][hereC] == 'O':
            res1 = (-1, -1)
            break
        elif board[hereR][hereC] == '.':
            preR, preC = hereR, hereC

    # 구슬 2 이동
    preR, preC = marble2
    while True:
        hereR, hereC = preR + dr[d], preC + dc[d]
        # 이동된 구슬 1을 만나거나 벽을 만나면 멈추기
        if (hereR, hereC) == res1 or board[hereR][hereC] == '#':
            res2 = (preR, preC)
            break
        elif board[hereR][hereC] == 'O':
            res2 = (-1, -1)
            break
        elif board[hereR][hereC] == '.':
            preR, preC = hereR, hereC

    return res1, res2


# d 방향으로 보드판을 기울일 때, 먼저 이동시켜야 하는 구슬을 판단하고 두 구슬을 이동시키는 함수
def rotateBoard(marble1, marble2, d):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    # 기울이는 방향으로 더 앞쪽에 있는 구슬 판단 후 먼저 이동시키기
    if marble1[0] * dr[d] + marble1[1] * dc[d] < marble2[0] * dr[d] + marble2[1] * dc[d]:
        res1, res2 = roll(marble1, marble2, d)
    else:
        res2, res1 = roll(marble2, marble1, d)

    return res1, res2


def getMinRotate():
    global board, isVisited, R, B

    queue = deque()
    queue.append((R, B, 0))
    isVisited[R[0]][R[1]][B[0]][B[1]] = 1

    while len(queue)>0:
        hereR, hereB, hereMove = queue.popleft()

        for d in range(4):
            nextR, nextB = rotateBoard(hereR, hereB, d)
            nextMove = hereMove + 1

            # 구슬 B가 구멍에 빠지면 실패
            if nextB == (-1,-1):
                continue
            # 구슬 R만 구멍에 빠지면 성공
            elif nextR == (-1,-1):
                return nextMove

            # 두 구슬 다 구멍에 빠지지 않았으며, 이전에 방문한 상태가 아니고, 이동 횟수가 10 미만일 때 queue에 추가
            if isVisited[nextR[0]][nextR[1]][nextB[0]][nextB[1]] == 0 and nextMove < 10:
                isVisited[nextR[0]][nextR[1]][nextB[0]][nextB[1]] = 1
                queue.append((nextR, nextB, nextMove))

    return -1


if __name__ == '__main__':
    H, W = map(int, input().split())
    board = []
    isVisited = [[[[0]*W for _ in range(H)] for _ in range(W)] for _ in range(H)]

    # 보드판을 입력받을 때 두 구슬의 위치 파악 & 빈 보드판으로 만들기
    for r in range(H):
        tmp = input().strip()
        board.append([*tmp])
        if 'R' in tmp:
            c = tmp.find('R')
            R = (r, c)
            board[r][c] = '.'
        if 'B' in tmp:
            c = tmp.find('B')
            B = (r, c)
            board[r][c] = '.'

    print(getMinRotate())