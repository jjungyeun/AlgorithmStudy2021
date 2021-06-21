def recursiveFunc(here, hereSum, N, board, minist):
    y, x = here
    if y == N-1 and x == N-1:
        return min(minist, hereSum)
    if hereSum >= minist:
        return 100000

    if x < N-1:
        minist = min(minist, recursiveFunc((y, x+1), hereSum + int(board[y][x+1]), N, board, minist))
    if y < N-1:
        minist = min(minist, recursiveFunc((y+1, x), int(hereSum + int(board[y+1][x])), N, board, minist))

    return minist


if __name__ == '__main__':
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        N = int(input())
        board = []
        for i in range(N):
            tmp = input()
            board.append(tmp.split(' '))

        res = recursiveFunc((0,0), int(board[0][0]), N, board, 100000)
        print("#%d %d" % (test_case, res))