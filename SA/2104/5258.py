def getBestChoice(W, M, S, P):
    memo = [[-1] * (W+1) for _ in range(M+1)]

    for i in range(M+1):  # i번째 물건
        for w in range(W+1):    # 현재 배낭 무게
            if i == 0 or w == 0:
                memo[i][w] = 0
            else:
                if S[i] > w:
                    memo[i][w] = memo[i-1][w]
                else:
                    memo[i][w] = max(memo[i-1][w-S[i]] + P[i], memo[i-1][w])

    return memo[M][W]


if __name__ == '__main__':
    TC = int(input())
    for T in range(1, TC + 1):
        N, M = map(int, input().split())
        S, P = [0], [0]
        for i in range(M):
            s_i, p_i = map(int, input().split())
            S.append(s_i)
            P.append(p_i)

        res = getBestChoice(N, M, S, P)
        print("#%d %d" % (T, res))