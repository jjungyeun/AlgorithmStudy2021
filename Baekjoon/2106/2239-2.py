def getPromisingNums(r, c):
    global boardRow, boardCol, boardSquare
    return [n for n in range(1, 10) if boardRow[r][n] and boardCol[c][n] and boardSquare[(r//3)*3 + (c//3)][n]]


def backtracking(depth):
    global board, blanks, isEnd, boardRow, boardCol, boardSquare

    if isEnd:
        return

    if depth == len(blanks):
        isEnd = True
        for row in board:
            for x in row:
                print(x, end='')
            print()
        return

    r, c = blanks[depth]
    for n in getPromisingNums(r, c):
        boardRow[r][n] = False
        boardCol[c][n] = False
        boardSquare[(r//3)*3 + (c//3)][n] = False
        board[r][c] = n
        backtracking(depth+1)
        boardRow[r][n] = True
        boardCol[c][n] = True
        boardSquare[(r//3)*3 + (c//3)][n] = True
        board[r][c] = 0


if __name__ == '__main__':
    board = []
    blanks = []
    isEnd = False

    # 각 행, 각 열, 각 정사각형에 들어갈 수 있는 숫자를 표시하는 배열
    boardRow, boardCol, boardSquare = [[True] * 10 for _ in range(9)], [[True] * 10 for _ in range(9)], [[True] * 10 for _ in range(9)]

    for i in range(9):
        tmp = list(map(int, list(input())))
        board.append(tmp)
        for j in range(9):
            here = tmp[j]
            if here == 0:
                blanks.append((i,j))
            else:
                boardRow[i][here] = False
                boardCol[j][here] = False
                boardSquare[(i//3)*3 + (j//3)][here] = False

    backtracking(0)