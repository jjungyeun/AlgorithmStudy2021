minist = 1000
isVisit = [0] * 100


def backTracking(here, cnt, rest_btr, N, btr_list):
    global minist

    # print(here, cnt, rest_btr)

    # 최소 횟수 넘은 경우
    if cnt >= minist:
        return

    # 배터리 다 떨어진 경우
    if rest_btr < 0:
        return

    # 도착 or 도착까지 배터리 충분한 경우
    if here == N-1 or rest_btr >= N - 1 - here:
        print("도착! cnt: ", cnt)
        print("충전소: ", end='')
        for i in range(len(isVisit)):
            if isVisit[i]:
                print(i, end=" ")
        print()
        minist = cnt
        return

    # 충전 안함
    backTracking(here+1, cnt, rest_btr - 1, N, btr_list)
    # 충전 함
    isVisit[here] = 1
    backTracking(here+1, cnt + 1, btr_list[here] - 1, N, btr_list)
    isVisit[here] = 0
    return


if __name__ == '__main__':
    TC = int(input())
    for T in range(1, TC + 1):
        minist = 1000
        tmp = list(map(int, input().split()))
        N = tmp[0]
        M = tmp[1:]

        print("\n--TC %d--" % T)
        backTracking(1, 0, M[0]-1, N, M)
        print("#%d %d" % (T, minist))