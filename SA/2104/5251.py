from queue import PriorityQueue
adj = []


def Dijkstra(start, V):
    global adj
    dist = [float('inf')] * (V+1)
    pq = PriorityQueue()

    dist[start] = 0
    pq.put((0, start))

    while not pq.empty():
        hereDist, here = pq.get()

        if hereDist > dist[here]:
            continue

        if here == V:
            continue

        for i in range(len(adj[here])):
            there = adj[here][i][0]
            thereDist = hereDist + adj[here][i][1]
            if thereDist < dist[there]:
                dist[there] = thereDist
                pq.put((thereDist, there))

    return dist[V]


if __name__ == '__main__':
    TC = int(input())
    for T in range(1, TC + 1):
        V, E = map(int, input().split())
        adj = [[] for _ in range(V+1)]
        for _ in range(E):
            v1, v2, w = map(int, input().split())
            adj[v1].append((v2, w))

        res = Dijkstra(0, V)
        print("#%d %d"%(T,res))