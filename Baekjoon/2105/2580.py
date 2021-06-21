import sys


def isPromising(r, c, num):
    global board

    # 가로 검사
    if num in board[r]:
        return False

    # 세로 검사
    for i in range(9):
        if board[i][c] == num:
            return False

    # 3x3 검사
    row = (r//3) * 3
    col = (c//3) * 3
    num_list = board[row][col:col+3] + board[row+1][col:col+3] + board[row+2][col:col+3]
    # print(num, num_list)
    if num in num_list:
        return False

    return True


def backTracking(depth):
    global blank, isSolved, board
    if isSolved:
        return

    if depth == len(blank):
        isSolved = True
        for row in board:
            for e in row:
                print(e, end=' ')
            print()
        return

    hereR, hereC = blank[depth]
    for i in range(1, 10):
        if isPromising(hereR, hereC, i):
            board[hereR][hereC] = i
            backTracking(depth+1)
            board[hereR][hereC] = 0


if __name__ == '__main__':
    board = []
    blank = []
    isSolved = False
    for i in range(9):
        tmp = list(map(int, sys.stdin.readline().split()))
        board.append(tmp)
        for j in range(9):
            if tmp[j] == 0:
                blank.append((i, j))

    backTracking(0)
