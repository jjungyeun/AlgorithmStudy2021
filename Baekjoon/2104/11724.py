# from collections import deque
# import sys
#
#
# def getConnectedComponent():
#     global N, adj, visited
#
#     queue = deque()
#     CC = 0
#
#     for i in range(1, N+1):
#         if visited[i] == 0:
#             visited[i] = 1
#             queue.append(i)
#             CC += 1
#
#             while len(queue) > 0:
#                 here = queue.popleft()
#                 for x in range(1, N+1):
#                     if visited[x] == 0 and adj[here][x] == 1:
#                         visited[x] = 1
#                         queue.append(x)
#
#     print(CC)
#
#
# if __name__ == '__main__':
#     N, M = map(int, input().split())
#     adj = [[0] * (N+1) for _ in range(N+1)]  # 간선 저장 배열
#     visited = [0] * (N+1)
#
#     for _ in range(M):
#         u, v = map(int, sys.stdin.readline().split())
#         adj[u][v] = adj[v][u] = 1
#
#     getConnectedComponent()

import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]  # 간선 저장 배열
visited = [0] * (N + 1)


def dfs(node):
    # print(node)
    global adj, visited

    for x in adj[node]:
        if not visited[x]:
            visited[x] = 1
            dfs(x)


def getConnectedComponent():
    global N, adj, visited
    CC = 0

    for i in range(1, N+1):
        if not visited[i]:
            CC += 1
            # print("%d번째 연결" % CC)
            visited[i] = 1
            dfs(i)

    # print("답")
    print(CC)

if __name__ == '__main__':

    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)

    getConnectedComponent()