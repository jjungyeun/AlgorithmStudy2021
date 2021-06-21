from queue import PriorityQueue


def getBefore(k):
    global nextNum
    before = k - 1
    while before != -1 and nextNum[before] != (k-before):
        before -= 1

    # print("getBefore(%d) = %d" % (k, before))
    return before


def deleteKth(k):
    # print("\ndeleteKth(%d)" % k)
    global nextNum, diff, pq, lastIdx
    before = getBefore(k)
    next = nextNum[k]
    # print("before: %d, next: %d" % (before, next))

    # k가 첫번째 숫자가 아닐 때
    if before != -1:
        # k가 마지막 숫자일 때
        if k == lastIdx:
            nextNum[before] = 0
            diff[before] = 0
            nextNum[k] = -1
            lastIdx = before
            return

        # k가 중간 숫자 일 때
        else:
            nextNum[before] += next
            diff[before] += diff[k]
            if diff[before] > 0:
                pq.put((before, getBefore(before)))

    if diff[k + next] > 0:
        pq.put((k + next, before))
    nextNum[k] = -1

    # print("current state: ", end='')
    # printAnswer()


def getMaxNumber():
    global K, nextNum, pq, lastIdx

    cnt = 0
    while cnt < K:
        if pq.empty():
            deleteKth(lastIdx)
        else:
            cand, befo = pq.get()

            # 현재 상태에서 의미 없어진 case
            if nextNum[cand] == -1 or nextNum[befo] == -1:
                continue

            deleteKth(cand)
        cnt += 1


def printAnswer():
    global nextNum
    i = 0
    while True:
        if nextNum[i] == -1:
            i += 1
            continue

        print(num[i], end='')

        if nextNum[i] == 0:
            break

        i += nextNum[i]
    print()


if __name__ == '__main__':
    N, K = map(int, input().split())
    num = input()
    pq = PriorityQueue()

    lastIdx = N-1
    nextNum = [1] * N   # i번째 수의 다음 수까지 몇칸 떨어져 있는 지 (숫자가 지워지는 경우에 필요), 지워진 숫자에는 -1로 표기
    nextNum[-1] = 0
    diff = [0] * (N)  # diff[i] = (i+1번째 수) - (i번째 수)
    for i in range(N-1):
        diff[i] = int(num[i+1]) - int(num[i])
        if diff[i] > 0:
            pq.put((i, i-1))

    getMaxNumber()
    printAnswer()


