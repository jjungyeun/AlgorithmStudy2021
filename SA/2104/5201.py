
def getMostWeight(N, M, w, t):
    isVisited = [0 for i in range(N)]
    weight = 0

    for t_i in t:
        for j in range(N-1, -1, -1):
            if isVisited[j] or t_i < w[j]:
                continue
            weight += w[j]
            isVisited[j] = 1
            break

    return weight


if __name__ == '__main__':
    TC = int(input())
    for T in range(1, TC + 1):

        N, M = map(int, input().split(' '))
        tmp = input().split(' ')
        w = [int(i) for i in tmp]
        tmp = input().split(' ')
        t = [int(i) for i in tmp]

        w.sort()
        t.sort()

        res = getMostWeight(N, M, w, t)
        print("#%d %d" % (T, res))