# (r, c)를 기준으로 붙일 수 있는 색종이의 최대 크기를 구하는 함수
def check_size(r, c):
    global board
    res = 1

    for d in range(1, 5):
        if r + d > 9 or c + d > 9:
            break

        size_up = True
        for row in board[r:r+d+1]:
            if row[c:c+d+1] != ['1' for _ in range(d+1)]:
                size_up = False
                break

        if size_up:
            res += 1
        else:
            break

    return res


# board에서 (r, c)를 기준으로 size만큼의 정사각형 범위를 num으로 채우는 함수
def fill(r, c, size, num):
    global board

    for rr in range(r, r+size):
        for cc in range(c, c+size):
            board[rr][cc] = num


# depth번째 1이 적힌 칸을 채우는 함수
def backtracking(depth, cnt):
    global board, paper, fill_area, min_cnt

    # 마지막칸까지 채우면 최소 색종이 개수 갱신
    if depth == len(fill_area):
        min_cnt = min(min_cnt, cnt)
        return

    # 지금까지 구한 최소 색종이 개수보다 커지면 종료
    if cnt >= min_cnt:
        return

    r, c = fill_area[depth]
    # 이전 칸에 의해 이미 채워졌으면 다음 칸으로 넘어가기
    if board[r][c] == '0':
        backtracking(depth+1, cnt)
        return
    size = check_size(r, c)

    # 현재 칸에 붙일 수 있는 색종이를 모두 붙여보기
    for s in range(size, 0, -1):
        if paper[s] > 0:
            fill(r, c, s, '0')
            paper[s] -= 1
            backtracking(depth+1, cnt+1)
            fill(r, c, s, '1')
            paper[s] += 1


def fill_board():
    global board, min_cnt

    backtracking(0, 0)

    if min_cnt == 30:
        return -1

    return min_cnt


if __name__ == '__main__':
    board = []
    paper = [0,5,5,5,5,5]
    fill_area = []
    min_cnt = 30

    for r in range(10):
        tmp = input().split()
        board.append(tmp)
        for c in range(10):
            if tmp[c] == '1':
                fill_area.append((r, c))

    print(fill_board())