from collections import deque

INF = float('inf')


def getMinPlugChange():
    global N, K, readyQueue

    changeCnt = 0
    onPlug = set()
    rest = dict()

    # 각 제품의 task list 구하기
    for i, task in enumerate(readyQueue):
        if task in rest:
            rest[task].append(i)
        else:
            rest[task] = deque([i])
    # 추후 정렬을 위해 task 없는 제품에는 무한대 저장
    for i in range(1, K+1):
        if i not in rest:
            rest[i] = deque([INF])

    for idx, nowTask in enumerate(readyQueue):
        # 이번 차례 제품이 콘센트에 꼽혀있지 않을 때
        if nowTask not in onPlug:
            # 콘센트 자리 남아있는 경우
            if len(onPlug) < N:
                onPlug.add(nowTask)
            # 콘센트 자리 없는 경우
            else:
                # 콘센트에 꼽혀있는 제품들의 남은 task list 불러와서
                # 가장 나중에 필요한 (또는 사용이 끝난) 제품 찾기
                temp_dict = {key: value for key, value in rest.items() if key in onPlug}
                rank = sorted(temp_dict.items(), key=lambda item: item[1][0], reverse=True)
                deleted = rank[0][0]
                onPlug.remove(deleted)
                onPlug.add(nowTask)
                changeCnt += 1

        # 이번 차례 제품의 rest list 갱신
        # 사용 끝났으면 무한대 넣어주기
        rest[nowTask].popleft()
        if len(rest[nowTask]) == 0:
            rest[nowTask].append(INF)

    return changeCnt


if __name__ == '__main__':
    N, K = map(int, input().split())
    readyQueue = list(map(int, input().split()))
    print(getMinPlugChange())
