minist = 10000
isVisit = [0] * 15


def backTracking(depth, cost, N, cost_mtrx):
    global minist, isVisit

    if cost >= minist:
        return

    if depth == N:
        minist = cost
        return

    for i in range(N):
        if not isVisit[i]:
            isVisit[i] = 1
            backTracking(depth+1, cost+cost_mtrx[depth][i], N, cost_mtrx)
            isVisit[i] = 0


if __name__ == '__main__':
    TC = int(input())
    for T in range(1, TC + 1):
        N = int(input())
        V = [0] * 15
        for i in range(N):
            V[i] = list(map(int, input().split()))

        minist = 10000
        backTracking(0, 0, N, V)
        print("#%d %d" % (T, minist))