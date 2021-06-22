from collections import deque


def bfs():
    global board, visited
    dx = [-1, 1, -3, 3]
    queue = deque()

    queue.append((board, 0))
    visited.add(board)

    while len(queue) > 0:
        here_state, here_cnt = queue.popleft()
        here_blank = here_state.index('0')

        # 정답이 되면 종료
        if here_state == '123456780':
            return here_cnt

        for d in range(4):
            # +1 또는 -1을 해줄때 행이 변하면 안됨
            if (d == 0 and here_blank in (3, 6)) or (d == 1 and here_blank in (2, 5)):
                continue

            dest = here_blank + dx[d]
            if 0 <= dest < 9:
                # blank 위치랑 dest 위치 숫자 swap
                new_state = ''
                target_num = here_state[dest]
                for i, x in enumerate(here_state):
                    if i == here_blank:
                        new_state += target_num
                    elif i == dest:
                        new_state += '0'
                    else:
                        new_state += x
                # 방문한 적 없는 배치면 방문
                if new_state not in visited:
                    queue.append((new_state, here_cnt + 1))
                    visited.add(new_state)

    return -1


if __name__ == '__main__':
    board = ''
    for _ in range(3):
        board += ''.join(input().split())
    visited = set(board)
    print(bfs())