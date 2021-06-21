def dfs(here, hereCost, isVisit, restRoom, N, cost, minist):
    if restRoom == 0:
        return min(minist, hereCost + int(cost[here][0]))
    if hereCost >= minist:
        return 100000

    for i in range(1, N):
        if isVisit[i] == 1:
            continue
        isVisit[i] = 1
        minist = min(minist, dfs(i, hereCost + int(cost[here][i]),isVisit, restRoom-1,N, cost, minist))
        isVisit[i] = 0

    return minist


if __name__ == '__main__':
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        N = int(input())
        cost = []
        isVisit = []
        for i in range(N):
            tmp = input()
            cost.append(tmp.split(' '))
            isVisit.append(0)

        res = dfs(0, 0, isVisit, N-1, N, cost, 100000)
        print("#%d %d" % (test_case, res))