test_case = 0
adj = [[0] * 101 for i in range(101)]
isVisit = []


def dfs(here, N):
    global test_case, adj, isVisit
    for i in range(1, N+1):
        if isVisit[i] != test_case and adj[here][i] == test_case: # 아직 방문 안했고 같은 그룹이면 방문
            isVisit[i] = test_case
            dfs(i, N)


def getGroups(N):
    global test_case, isVisit
    res = 0
    for i in range(1, N+1):
        if isVisit[i] != test_case: # 아직 방문 안했으면 방문
            isVisit[i] = test_case
            dfs(i, N)
            res += 1
    return res


if __name__ == '__main__':
    TC = int(input())
    for T in range(1, TC + 1):
        test_case = T
        N, M = map(int, input().split())
        tmp = list(map(int, input().split()))

        isVisit = [0] * (N+1)
        for i in range(0, 2*M, 2):
            a, b = tmp[i], tmp[i+1]
            adj[a][b] = adj[b][a] = test_case

        res = getGroups(N)
        print("#%d %d" % (T, res))