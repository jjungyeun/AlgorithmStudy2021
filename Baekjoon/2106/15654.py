import sys


def dfs(cnt):
    global N, M, num_list, visited

    if cnt == M:
        sys.stdout.write(' '.join(answer) + '\n')
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            answer.append(str(num_list[i]))
            dfs(cnt+1)
            visited[i] = 0
            answer.pop()


if __name__ == '__main__':
    N, M = map(int, input().split())
    num_list = sorted(list(map(int, sys.stdin.readline().split())))
    visited = [0 for _ in range(N)]
    answer = []

    dfs(0)