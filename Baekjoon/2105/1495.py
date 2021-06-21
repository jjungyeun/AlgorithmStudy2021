def getNextVolume(hereList, dv, M):
    nextVolume = [0 for _ in range(M+1)]
    maximum = -1
    for i in range(M+1):
        if hereList[i] == 1:
            if i + dv <= M:
                nextVolume[i + dv] = 1
                maximum = max(maximum, i + dv)
            if i - dv >= 0:
                nextVolume[i - dv] = 1
                maximum = max(maximum, i - dv)
    return nextVolume, maximum


def getMaxVolume(N, S, M, V):
    hereList = [0 for _ in range(S)] + [1] + [0 for _ in range(M-S)]
    for i in range(N):
        hereList, maximum = getNextVolume(hereList, V[i], M)
        # print(hereList, maximum)
        if maximum == -1:
            print(-1)
            return
    print(maximum)


if __name__ == '__main__':
    N, S, M = map(int, input().split())
    V = list(map(int, input().split()))

    getMaxVolume(N, S, M, V)