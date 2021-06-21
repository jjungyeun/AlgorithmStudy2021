## BFS

from collections import deque


def getMinOperation():
    global N, visited
    queue = deque()
    queue.append((N, 0))
    visited[N] = -1

    while len(queue) > 0:
        hereNum, hereCnt = queue.popleft()

        if hereNum == 1:
            print(hereCnt)
            return

        if hereNum % 3 == 0 and visited[hereNum//3] == 0:
            queue.append((hereNum//3, hereCnt+1))
            visited[hereNum//3] = hereNum

        if hereNum % 2 == 0 and visited[hereNum//2] == 0:
            queue.append((hereNum//2, hereCnt+1))
            visited[hereNum//2] = hereNum

        if visited[hereNum-1] == 0:
            queue.append((hereNum-1, hereCnt+1))
            visited[hereNum-1] = hereNum


def getpath():
    global N, visited
    path = [1]

    here = 1
    while here != N:
        path.append(visited[here])
        here = visited[here]

    path.reverse()
    for x in path:
        print(x, end=' ')


if __name__ == '__main__':
    N = int(input())
    visited = [0 for _ in range(N+1)]

    getMinOperation()
    getpath()




# ## Dynamic Programming
#
# def getMinOperation():
#     global N, dist, path
#
#     for i in range(2, N+1):
#         dist[i] = dist[i-1] + 1
#         path[i] = i-1
#
#         if i % 2 == 0 and dist[i//2] + 1 < dist[i]:
#             dist[i] = dist[i//2] + 1
#             path[i] = i//2
#
#         if i % 3 == 0 and dist[i//3] + 1 < dist[i]:
#             dist[i] = dist[i//3] + 1
#             path[i] = i//3
#
#     print(dist[N])
#
#
# def getpath():
#     global N, path
#
#     here = N
#     while here != 0:
#         print(here, end=' ')
#         here = path[here]
#
#
# if __name__ == '__main__':
#     N = int(input())
#     dist = [0 for _ in range(N+1)]
#     path = [0 for _ in range(N+1)]
#
#     getMinOperation()
#     getpath()