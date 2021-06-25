import sys


def get_max_delivery():
    global N, C, delivery_list, box_on_truck

    delivered = 0
    for here in range(1, N+1):
        # 현재 마을에 내릴 박스 내리기
        delivered += box_on_truck[here]

        rest = C
        # 트럭에 자리 있으면 배달지 가까운 순으로 싣기
        for i in range(here+1, N+1):
            if rest > 0:
                # 싣고 있던거 그대로 놔두기
                if box_on_truck[i] > rest:
                    box_on_truck[i] = rest
                rest -= (box_on_truck[i])

                # 새로 싣기
                if delivery_list[here][i] > rest:
                    box_on_truck[i] += rest
                    rest = 0
                else:
                    box_on_truck[i] += delivery_list[here][i]
                    rest -= (delivery_list[here][i])
            else:
                box_on_truck[i] = 0

    return delivered


if __name__ == '__main__':
    N, C = map(int, input().split())
    M = int(input())
    delivery_list = [[0 for _ in range(N+1)] for _ in range(N+1)]
    box_on_truck = [0 for _ in range(N+1)]

    for _ in range(M):
        f, t, b = map(int, sys.stdin.readline().split())
        delivery_list[f][t] = b

    print(get_max_delivery())
