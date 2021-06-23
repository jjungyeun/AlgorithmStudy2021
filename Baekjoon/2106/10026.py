# start 좌표를 기준으로 같은 색인 칸들을 방문하는 함수
def visit_area(start, color, tc):
    global N, board, visited
    dr, dc = [1,-1,0,0], [0,0,1,-1]
    r, c = start

    stack = [(r, c)]

    while stack:
        here_r, here_c = stack.pop()

        if visited[here_r][here_c] == tc:
            continue

        visited[here_r][here_c] = tc

        # 두번째 tc(적록색약)에서 색 구분을 없애기 위해 G를 모두 R로 변경
        if color == 'G':
            board[here_r][here_c] = 'R'

        # 아직 방문한적 없고 색이 같으면 스택에 넣기
        for d in range(4):
            next_r, next_c = here_r + dr[d], here_c + dc[d]
            if 0 <= next_r < N and 0 <= next_c < N and visited[next_r][next_c] != tc and board[next_r][next_c] == color:
                stack.append((next_r, next_c))


# 방문한적 없는 새로운 칸들을 방문하며 구역 수를 구하는 함수
def get_areas(tc):
    global N, board

    res = 0
    for r in range(N):
        for c in range(N):
            # 방문한적 없는 칸 방문하고 구역 수 증가 시키기
            if visited[r][c] != tc:
                res += 1
                visit_area((r, c), board[r][c], tc)

    return res


if __name__ == '__main__':
    N = int(input())
    board = []
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for _ in range(N):
        tmp = input().strip()
        board.append([*tmp])

    print(get_areas(1), end=' ')
    print(get_areas(2))

