from queue import PriorityQueue


# a번과 b번 우주신 연결
def linkTwoSG(a, b):
    global groupNum, unlinkedSG, restGroup

    # 둘 다 그룹 없음 -> 숫자 큰 애 기준으로 그룹 생성
    if groupNum[a] == 0 and groupNum[b] == 0:
        g = max(a, b)
        groupNum[a] = groupNum[b] = g
        unlinkedSG -= 2
        restGroup += 1

    # 한 개만 그룹 있음 -> 그룹 있는 애랑 같은 그룹으로 들어가기
    elif groupNum[a] == 0 or groupNum[b] == 0:
        g = max(groupNum[a], groupNum[b])
        groupNum[a] = groupNum[b] = g
        unlinkedSG -= 1

    # 둘 다 그룹 있음 -> 번호 더 큰 그룹으로 합체
    else:
        g = max(groupNum[a], groupNum[b])
        before_g = min(groupNum[a], groupNum[b])
        for i in range(1, len(groupNum)):
            if groupNum[i] == before_g:
                groupNum[i] = g
        restGroup -= 1


def Kruskal():
    global PQ, groupNum, unlinkedSG
    res = 0

    while not PQ.empty():
        dist, SG1, SG2 = PQ.get()

        # 모든 우주신 연결 되고, 다 같은 그룹에 속하면 종료
        if unlinkedSG <= 0 and restGroup == 1:
            break

        # 둘이 같은 그룹이면 (사이클 생성되면) 패스
        if groupNum[SG1] != 0 and groupNum[SG1] == groupNum[SG2]:
            continue

        # 두 우주신 연결
        linkTwoSG(SG1, SG2)
        res += dist

    return res

if __name__ == '__main__':
    N, M = map(int, input().split())
    PQ = PriorityQueue()
    location = [0] * (N+1)
    groupNum = [0] * (N+1)
    unlinkedSG = N
    restGroup = 0
    for i in range(1, N+1):
        x, y = map(int, input().split())
        location[i] = (x, y)

    for _ in range(M):
        s, d = map(int, input().split())
        linkTwoSG(s, d)

    for i in range(1, N+1):
        x_i, y_i = location[i]
        for j in range(i+1, N+1):
            x_j, y_j = location[j]
            dx = abs(x_i - x_j)
            dy = abs(y_i - y_j)
            dist = (dx*dx + dy*dy)**0.5
            PQ.put((dist, i, j))

    print("%.2f" % Kruskal())