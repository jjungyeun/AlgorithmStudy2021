# f(n, k): n자리이며 1의자리가 k인 오르막수의 개수
# f(n, k) = 1 (n=1 or k=0)
#         = f(n, k-1) + f(n-1, k) (n>1 and k>0)
def getAscendingNum(N):
    global memo

    for k in range(10):
        memo[1][k] = 1

    for n in range(2, N+1):
        memo[n][0] = 1
        for k in range(1, 10):
            memo[n][k] = memo[n-1][k] + memo[n][k-1]

    res = 0
    for k in range(10):
        res += memo[N][k]

    print(res % 10007)


if __name__ == '__main__':
    N = int(input())
    memo = [[-1] * 10 for _ in range(N+1)]

    getAscendingNum(N)