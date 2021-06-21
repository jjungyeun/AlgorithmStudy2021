memo = [0] * 31


# 점화식: f(n) = f(n-3) + 2*f(n-2) + f(n-1)
def getTileTypes(N):
    global memo
    if memo[N] != 0:
        return memo[N]

    for i in range(4, N+1):
        if memo[i] != 0:
            continue
        memo[i] = memo[i-3] + 2 * memo[i-2] + memo[i-1]

    return memo[N]


if __name__ == '__main__':
    memo[1] = 1
    memo[2] = 3
    memo[3] = 6

    TC = int(input())
    for T in range(1, TC + 1):
        N = int(input())
        res = getTileTypes(N)
        print("#%d %d" % (T, res))
