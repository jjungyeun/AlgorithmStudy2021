N, M = map(int, input().split())
visited = [0] * (N+1)


def dfs(depth, cnt):
    if cnt == M:
        for idx in range(1, N+1):
            if visited[idx] == 1:
                print(idx, end=' ')
        print()
        return

    if depth == N+1:
        return

    # depth 넣는 경우
    visited[depth] = 1
    dfs(depth+1, cnt+1)
    visited[depth] = 0
    # depth 안 넣는 경우
    dfs(depth+1, cnt)


dfs(1, 0)