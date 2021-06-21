# 그룹 s, d 합치기 (그룹 s의 도시들을 모두 그룹 d로 변경)
def mergeGroup(s, d):
    global cityGroup
    for i in range(len(cityGroup)):
        if cityGroup[i] == s:
            cityGroup[i] = d


# city에 방문하여 group을 표기하고, 인접한 다른 도시들도 방문
def dfs(city, group):
    global N, adj, cityGroup

    cityGroup[city] = group

    for i, isReachable in enumerate(adj[city]):
        if isReachable:
            # 아직 방문하지 않은 도시라면 같은 그룹으로 방문
            if cityGroup[i] == 0:
                dfs(i, group)
            # 이미 방문했던 도시이며, 현재 도시와 다른 그룹이라면 그 그룹과 합치기 (재방문 X)
            elif cityGroup[i] != group:
                mergeGroup(group, cityGroup[i])


# 모든 여행 계획 도시들에 갈 수 있는지 구하는 함수
def isTravelable():
    global N, adj, cityGroup, plan
    groupCnt = 0

    # 분리된 도시들마다 그룹 번호 붙이기
    for i in range(N):
        # 아직 방문하지 않은 도시라면 새 그룹 생성 및 방문
        if cityGroup[i] == 0:
            groupCnt += 1
            dfs(i, groupCnt)

    # 여행갈 도시들이 모두 한 그룹에 있으면 True, 아니면 False 반환
    planGroup = 0
    for city in plan:
        hereCity = city - 1
        if cityGroup[hereCity] != planGroup:
            if planGroup == 0:
                planGroup = cityGroup[hereCity]
            else:
                return False

    return True


if __name__ == '__main__':
    N = int(input())
    M = int(input())
    cityGroup = [0 for _ in range(N)]

    adj = []
    for _ in range(N):
        adj.append(list(map(int, input().split())))

    plan = set(map(int, input().split()))

    if isTravelable():
        print("YES")
    else:
        print("NO")