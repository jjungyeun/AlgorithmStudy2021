memo = [[-1] * 71 for _ in range(71)]


# 점화식: f[n][k] = f[n-1][k-1] + f[n-1]f[k]
def getCoefficient(n, k):
    global memo
    if memo[n][k] != -1:
        return memo[n][k]

    for i in range(1, n+1):
        for j in range(1, min(i, k) + 1):
            if memo[i][j] == -1:
                memo[i][j] = memo[i-1][j-1] + memo[i-1][j]

    return memo[n][k]


if __name__ == '__main__':

    for i in range(0, 71):
        memo[i][i] = 1
        memo[i][0] = 1

    TC = int(input())
    for T in range(1, TC + 1):
        N, a, b = map(int, input().split())
        res = getCoefficient(N, min(a, b))
        print("#%d %d" % (T, res))
