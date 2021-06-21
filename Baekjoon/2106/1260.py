from collections import deque
import sys


def dfs():
    global N, V, adj

    stack = [V]

    while len(stack) > 0:
        here = stack.pop()
        if visited[here]:
            continue
        visited[here] = 1

        print(here, end=' ')

        for next in range(N, 0, -1):
            if adj[here][next] and not visited[next]:
                stack.append(next)

    print()


def bfs():
    global N, V, adj, visited

    queue = deque()
    queue.append(V)
    visited[V] = 2

    while len(queue) > 0:
        here = queue.popleft()
        print(here, end=' ')

        for next in range(1, N + 1):
            if adj[here][next] and visited[next] != 2:
                queue.append(next)
                visited[next] = 2


if __name__ == '__main__':
    N, M, V = map(int, input().split())
    adj = [[0 for _ in range(N+1)] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        adj[a][b] = adj[b][a] = 1

    dfs()
    bfs()