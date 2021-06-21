from queue import PriorityQueue

dist = []
H = []


def nextTile(y, x, direction):
    if direction == 0:  # y 증가
        return y+1, x
    elif direction == 1:    # x 증가
        return y, x+1
    elif direction == 2:    # y 감소
        return y-1, x
    elif direction == 3:    # x 감소
        return y, x-1


def Dijkstra(start_y, start_x, N):
    global dist, H
    # 모든 정점의 최단거리를 무한대로 초기화
    dist = [[float('inf')] * N for _ in range(N)]
    pq = PriorityQueue()

    # 시작 정점 등록
    dist[start_y][start_x] = 0
    pq.put((0, (0, 0)))

    while pq:
        hereDist, tup = pq.get()
        hereY, hereX = tup

        # 도착하면 끝내기
        if hereY == hereX == N-1:
            break

        # 더 짧은 거리로 온적 있는 곳이면 패스
        if dist[hereY][hereX] < hereDist:
            continue

        # 상하좌우 이동해보기
        for i in range(4):
            thereY, thereX = nextTile(hereY, hereX, i)
            if 0 <= thereY < N and 0 <= thereX < N:
                # 높이 차이 구하기
                heightDiff = H[thereY][thereX] - H[hereY][hereX]
                if heightDiff < 0:
                    heightDiff = 0

                # 새로운 곳 거리 = 현재까지의 거리 + 높이차이 + 기본 이동값
                thereDist = hereDist + heightDiff + 1

                # 새로 갈 곳에 더 짧은 거리로 갈 수 있으면 거리 업뎃 및 정점 등록
                if dist[thereY][thereX] > thereDist:
                    dist[thereY][thereX] = thereDist
                    pq.put((thereDist, (thereY, thereX)))

    return dist[N-1][N-1]


if __name__ == '__main__':
    TC = int(input())
    for T in range(1, TC + 1):
        N = int(input())
        H = []
        for _ in range(N):
            H.append(list(map(int, input().split())))

        res = Dijkstra(0,0,N)
        print("#%d %d"%(T,res))