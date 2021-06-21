import heapq

heap = []
weight = 0


def union(parent, child, arr):
    root = arr[parent]


    if arr[child] == -1:
        arr[child] = root
        return arr

    leaf = arr[child]
    for i in range(len(arr)):
        if arr[i] == leaf:
            arr[i] = root

    return arr


def getMST(N):
    global heap, weight
    selected = [-1] * (N)
    cnt = 0
    res = 0

    while heap:
        if cnt == N - 1:
            break

        w, v1, v2 = heapq.heappop(heap)

        # cycle 생기면 패스
        if selected[v1] != -1 and selected[v1] == selected[v2]:
            continue

        # 트리 합체
        if selected[v1] == selected[v2]:
            selected[v1] = selected[v2] = max(v1, v2)
        elif selected[v1] > selected[v2]:
            selected = union(v1, v2, selected)
        else:
            selected = union(v2, v1, selected)

        # print("(%d, %d): %d"%(v1, v2, w))
        # print(selected)

        cnt += 1
        res += w

    return res


if __name__ == '__main__':
    TC = int(input())
    for T in range(1, TC + 1):
        V, E = map(int, input().split())
        weight = 0
        heap = []
        for _ in range(E):
            v1, v2, w = map(int, input().split())
            heapq.heappush(heap, (w, v1, v2))   # (가중치, 정점1, 정점2)

        res = getMST(V+1)
        print("#%d %d" % (T, res))