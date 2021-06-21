cnt = 0


def boundDFS(depth, N, rest, R):
    global cnt
    if rest == 0 or rest == R:
        cnt += 1
        return
    if depth == 1 or rest > R or rest < 0:
        return

    # i를 선택하는 경우
    boundDFS(depth-1, N, rest - depth, R - depth)
    # i를 선택 안 하는 경우
    boundDFS(depth-1, N, rest, R - depth)


def getSubsets(N, K):
    global cnt
    cnt = 0
    boundDFS(N, N, K, int((N*(N+1))/2))


if __name__ == '__main__':
    TC = int(input())
    for T in range(1, TC + 1):
        N, K = map(int, input().split())
        getSubsets(N, K)
        print("#%d %d"%(T, cnt))