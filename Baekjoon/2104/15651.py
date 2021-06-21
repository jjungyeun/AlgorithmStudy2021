def dfs(hereSeq, maxNum, maxLen):
    if len(hereSeq) == maxLen:
        for x in hereSeq:
            print(x, end=' ')
        print()
        return

    for i in range(1, maxNum + 1):
        dfs(hereSeq + [i], maxNum, maxLen)


if __name__ == '__main__':
    N, M = map(int, input().split())
    dfs([], N, M)
