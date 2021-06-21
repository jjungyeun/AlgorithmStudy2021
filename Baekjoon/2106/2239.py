def getPromisingNums(r, c):
    global board
    res = [False] + [True for _ in range(9)]

    for k in range(9):
        res[int(board[r][k])] = False
        res[int(board[k][c])] = False

    for i in range(3*(r//3),3*(r//3)+3):
        for j in range(3*(c//3),3*(c//3)+3):
            res[int(board[i][j])] = False

    return [str(idx) for idx, _ in enumerate(res) if _]


def backtracking(depth):
    global board, blanks, isEnd

    if isEnd:
        return

    if depth == len(blanks):
        isEnd = True
        for x in board:
            print(''.join(x))
        return

    r, c = blanks[depth]
    for n in getPromisingNums(r, c):
        board[r][c] = n
        backtracking(depth+1)
    board[r][c] = '0'


if __name__ == '__main__':
    board = []
    blanks = []
    isEnd = False

    for i in range(9):
        tmp = list(input())
        board.append(tmp)
        for j in range(9):
            if tmp[j] == '0':
                blanks.append((i,j))

    backtracking(0)


