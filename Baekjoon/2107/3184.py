from collections import deque


# (r,c)를 포함하는 영역을 탐색하며 양과 늑대의 수를 센다.
def bfs(r, c):
    global R, C, board, visited, now_sheep, now_wolf

    dr, dc = [1,-1,0,0], [0,0,1,-1]
    queue = deque()

    # 시작점 세팅
    queue.append((r, c))
    visited[r][c] = 1

    while len(queue) > 0:
        here_r, here_c = queue.popleft()

        # 현재 칸이 양이면 양 수 증가, 늑대면 늑대 수 증가 시키기
        if board[here_r][here_c] == 'o':
            now_sheep += 1
        elif board[here_r][here_c] == 'v':
            now_wolf += 1

        # 상하좌우로 이동가능한 칸이면 방문
        for d in range(4):
            next_r, next_c  = here_r + dr[d], here_c + dc[d]
            if 0 <= next_r < R and 0 <= next_c < C and board[next_r][next_c] != '#' and visited[next_r][next_c] == 0:
                visited[next_r][next_c] = 1
                queue.append((next_r, next_c))


# 하루가 지난 후의 결과를 반환한다.
def next_morning():
    global R, C, board, visited, now_sheep, now_wolf, total_sheep, total_wolf

    for r in range(R):
        for c in range(C):
            # 울타리가 아니고 방문한 적 없는 영역을 탐색
            if board[r][c] != '#' and visited[r][c] == 0:
                now_sheep, now_wolf = 0, 0
                bfs(r, c)
                # 탐색 후 해당 영역의 양과 늑대의 수를 비교
                if now_sheep > now_wolf:
                    total_sheep += now_sheep
                else:
                    total_wolf += now_wolf

    print("%d %d" % (total_sheep, total_wolf))


if __name__ == '__main__':
    R, C = map(int, input().split())
    board = [[*input()] for _ in range(R)]
    visited = [[0 for _ in range(C)] for _ in range(R)]
    now_sheep, now_wolf = 0, 0
    total_sheep, total_wolf = 0, 0

    next_morning()