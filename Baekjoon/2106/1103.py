# Python3로 제출 시 RecursionError 발생
# import sys
# sys.setrecursionlimit(10**9)

def goNext(r, c, step, d):
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]

    return r + step * dr[d], c + step * dc[d]


def getMaxMove(r, c, move):
    global N, M, board, visited, checkCycle, max_move

    visited[r][c] = move
    max_move = max(max_move, move)

    for d in range(4):
        if max_move == -1:
            return
        nextR, nextC = goNext(r, c, int(board[r][c]), d)
        nextMove = move + 1
        if 0 <= nextR < N and 0 <= nextC < M and board[nextR][nextC] != 'H':
                if checkCycle[nextR][nextC]:
                    max_move = -1
                    return
                elif visited[nextR][nextC] == 0 or visited[nextR][nextC] < nextMove:
                    checkCycle[nextR][nextC] = 1
                    getMaxMove(nextR, nextC, nextMove)
                    checkCycle[nextR][nextC] = 0


if __name__ == '__main__':
    N, M = map(int, input().split())
    board = []
    checkCycle = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    max_move = 0

    for _ in range(N):
        board.append([*input()])

    visited[0][0] = checkCycle[0][0] = 1
    getMaxMove(0,0,1)
    print(max_move)