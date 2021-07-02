# t(0): 물고기 이동, t(1): 물고기 위치 복구
def move_fishes(shark_r, shark_c,t, state):
    global position_fishes, board, dr, dc

    new_state = [*state]

    if t == 0:
        order = [i for i in range(1,17)]
    else:
        order = [i for i in range(16, 0, -1)]

    # 물고기 차례대로 이동
    for fish in order:
        fish_r, fish_c = position_fishes[fish][0], position_fishes[fish][1]
        fish_d = int(new_state[4*fish_r+fish_c])

        # 이미 잡아먹힌 물고기면 패스
        if (fish_r, fish_c) == (-1,-1):
            continue

        cnt = 0
        while True:
            # 모든 방향으로 이동할 수 없는 경우 패스
            if cnt == 8:
                break

            there_r, there_c = fish_r + dr[t][fish_d], fish_c + dc[t][fish_d]

            # 이동할 수 있는 칸일 때
            if 0 <= there_r < 4 and 0 <= there_c < 4 and (there_r, there_c) != (shark_r, shark_c):
                there_fish = board[there_r][there_c]

                # 이동할 칸으로 자리 교환
                board[fish_r][fish_c] = there_fish
                board[there_r][there_c] = fish
                position_fishes[fish] = [there_r, there_c]
                position_fishes[there_fish] = [fish_r, fish_c]
                new_state[4*fish_r+fish_c], new_state[4*there_r+there_c] = new_state[4*there_r+there_c], str(fish_d)
                break

            # 이동할 수 없는 칸이면 45도 회전
            else:
                fish_d += 1
                if fish_d == 9:
                    fish_d = 1
                cnt += 1

    return ''.join(new_state)


def eat_fish(r, c):
    global position_fishes, board

    eaten_fish = board[r][c]
    board[r][c] = 0
    position_fishes[eaten_fish] = [-1, -1]

    return eaten_fish


def repair_fish(r, c, fish):
    global position_fishes, board

    board[r][c] = fish
    position_fishes[fish] = [r, c]


def dfs(shark, current_sum, state):
    global position_fishes, board, max_sum, dr, dc

    shark_r, shark_c = shark
    shark_d = int(state[4*shark_r+shark_c])
    eaten_fish = eat_fish(shark_r, shark_c)

    # 상어 움직이기 전에 물고기 먼저 이동
    moved_state = move_fishes(shark_r, shark_c, 0, state)

    can_eat = False
    for i in range(1, 4):
        there_r, there_c = shark_r + dr[0][shark_d] * i, shark_c + dc[0][shark_d] * i

        # 이동할 칸에 물고기가 있으면 잡아먹으러 이동
        if 0 <= there_r < 4 and 0 <= there_c < 4 and board[there_r][there_c] > 0:
            can_eat = True
            there_fish = board[there_r][there_c]
            dfs((there_r, there_c), current_sum + there_fish, moved_state)

    # 잡아먹을 물고기 없으면 지금까지 먹은 물고기 합 저장하고 집에 가기
    if not can_eat:
        max_sum = max(max_sum, current_sum)

    # 물고기 되돌리기
    move_fishes(shark_r, shark_c, 1, moved_state)
    repair_fish(shark_r, shark_c, eaten_fish)


def play_game(start):
    global position_fishes, board

    current_sum = board[0][0]
    dfs((0, 0), current_sum, start)


if __name__ == '__main__':
    direction = [*'012345678']
    dr, dc = [[0,-1,-1,0,1,1,1,0,-1],[0,1,1,0,-1,-1,-1,0,1]], [[0,0,-1,-1,-1,0,1,1,1],[0,0,1,1,1,0,-1,-1,-1]]
    position_fishes = [[] for _ in range(17)]   # [r, c] 저장
    board = [[0 for _ in range(4)] for _ in range(4)]   # 0이면 빈칸, 1~16이면 해당 번호 물고기
    start_state = ''

    max_sum = 0

    for i in range(4):
        tmp = list(map(int, input().split()))
        for j in range(4):
            position_fishes[tmp[2 * j]] = [i, j]
            board[i][j] = tmp[2*j]
            start_state += direction[tmp[2*j + 1]]

    play_game(start_state)
    print(max_sum)
