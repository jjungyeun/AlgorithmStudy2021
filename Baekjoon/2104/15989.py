def get123Sum(n):
    global memo
    if memo[n] != 0:
        print(memo[n])
        return

    for i in range(1, n+1):
        if memo[i] != 0:
            continue

        if i <= 3:
            memo[i] = i
            continue

        k = i - 3
        if k % 2 == 0:  # k가 짝수일 때
            memo[i] = memo[k] + k//2 + 2
        else:           # k가 홀수일 때
            memo[i] = memo[k] + k // 2 + 3

    print(memo[n])


if __name__ == '__main__':
    TC = int(input())
    memo = [0] * 10001
    for T in range(TC):
        get123Sum(int(input()))