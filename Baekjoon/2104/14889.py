member_set = set()


# 가능한 멤버 구성의 경우를 모두 구하는 함수
def getMemList(depth, N, cnt_0, cnt_1, arr):
    if depth == N:
        member_set.add(''.join(arr))
        return

    if cnt_0 > 0:
        getMemList(depth+1, N, cnt_0-1, cnt_1, arr+['0'])
    if cnt_1 > 0:
        getMemList(depth+1, N, cnt_0, cnt_1-1, arr+['1'])


# 두 팀의 능력치의 차이를 구하는 함수
def getDiff(team1, team2, N, S):
    n = int(N/2)
    score1 = score2 = 0
    for i in range(n):
        for j in range(i, n):
            score1 += S[team1[i]][team1[j]]
            score2 += S[team2[i]][team2[j]]

    return abs(score1 - score2)


# 능력치 차이의 최소값을 구하는 함수
def findMinistDiff(N, S):
    global member_set
    getMemList(0, N, int(N/2), int(N/2), [])

    minist = 1000
    for mem in member_set:
        start_mem = [i for i in range(len(mem)) if mem[i] == '0']
        link_mem = [i for i in range(len(mem)) if mem[i] == '1']
        minist = min(minist, getDiff(start_mem, link_mem, N, S))

    return minist

if __name__ == '__main__':
    N = int(input())
    S = [0] * N
    for i in range(N):
        S[i] = list(map(int, input().split()))

    # S[i][j] + S[j][i] 미리 계산해놓기
    for i in range(N):
        for j in range(i,N):
            sum_ij = S[i][j] + S[j][i]
            S[i][j] = S[j][i] = sum_ij

    res = findMinistDiff(N, S)
    print(res)