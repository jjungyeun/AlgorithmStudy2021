from collections import deque


# BFS를 이용하여 (0,0)부터 (N-1, M-1)까지 가는 최소 이동 횟수를 구하는 함수
def getMinDist():
    global N, M, board, visited

    queue = deque()
    queue.append((0, 0, 1)) # 시작점 추가
    visited[0][0] = 1
    dr, dc = [1,-1,0,0], [0,0,1,-1]

    while len(queue) > 0:
        hereR, hereC, hereDist = queue.popleft()

        # 도착하면 종료
        if (hereR, hereC) == (N-1, M-1):
            return hereDist

        # 상하좌우 이동 가능한지 확인
        for d in range(4):
            thereR, thereC = hereR + dr[d], hereC + dc[d]
            thereDist = hereDist + 1

            # 보드판 내에 있는지, 이동 가능한 칸인지, 이전에 방문하지는 않았는지 확인 후 큐에 추가
            if 0 <= thereR < N and 0 <= thereC < M and board[thereR][thereC] == '1' and visited[thereR][thereC] == 0:
                visited[thereR][thereC] = 1
                queue.append((thereR, thereC, thereDist))


if __name__ == '__main__':
    N, M = map(int, input().split())
    board = []
    visited = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(N):
        board.append([*input()])

    print(getMinDist())