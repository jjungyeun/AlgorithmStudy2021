def makeAscendingScore():
    global N, level

    cnt = 0
    pre = level[-1]
    for i in range(N-2, -1, -1):
        if level[i] >= pre:
            newScore = pre-1
            cnt += (level[i] - newScore)
            pre = newScore
        else:
            pre = level[i]

    print(cnt)


if __name__ == '__main__':
    N = int(input())
    level = []
    for _ in range(N):
        level.append(int(input()))

    makeAscendingScore()