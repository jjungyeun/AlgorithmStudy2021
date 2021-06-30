from collections import deque
from itertools import combinations


def get_killable_enemy(archer_r, archer_c):
    global M, D, board

    visited = [[0 for _ in range(M)] for _ in range(archer_r+1)]
    dr, dc = [0, -1, 0], [-1, 0, 1]
    res = []

    queue = deque()
    queue.append((archer_r, archer_c, 0))
    visited[archer_r][archer_c] = 1

    while len(queue) > 0:
        here_r, here_c, here_dist = queue.popleft()

        if here_dist >= D:
            continue

        # 왼쪽, 위, 오른쪽 방문 확인
        for d in range(3):
            next_r, next_c = here_r + dr[d], here_c + dc[d]
            if 0 <= next_r < archer_r and 0 <= next_c < M and not visited[next_r][next_c]:
                # 다음 위치에 적이 있으면 결과 배열에 추가
                if board[next_r][next_c] == 1:
                    res.append((next_r, next_c))

                # 방문 표시하고 큐에 추가
                visited[next_r][next_c] = 1
                queue.append((next_r, next_c, here_dist+1))

    return res


def execute_game(archers):
    global N, M, kill

    # 게임에서 제외된 적들의 좌표
    killed = set()

    # 매 차례마다
    for turn in range(N):
        # 이번 차례에서 무찌른 적들의 좌표
        killed_this_turn = set()

        # 각 궁수마다
        for archer in archers:
            # 이번 차례에 무찌를 수 있는 적 중 아직 제외되지 않은 첫번째 적을 무찌른다.
            for enemy in kill[archer][turn]:
                if enemy not in killed:
                    killed_this_turn.add(enemy)
                    break

        # 이번 차례에서 무찌른 적들 제외하기
        killed = killed | killed_this_turn

    return len(killed)


def get_kill_cnt():
    global N, M, D, board, kill

    res = 0

    # 각 위치의 궁수가 무찌를 수 있는 적들의 좌표를 구한다.
    for r in range(N, 0, -1):
        for c in range(M):
            kill[c].append(get_killable_enemy(r, c))

    # 궁수를 배치하는 모든 경우의 수에 대해 무찌른 적의 수를 구한다.
    comb = list(combinations([i for i in range(M)], 3))
    for archers in comb:
        res = max(res, execute_game(archers))

    return res


if __name__ == '__main__':
    N, M, D = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    board.append([0 for _ in range(M)])
    kill = [[] for _ in range(M)]

    print(get_kill_cnt())
