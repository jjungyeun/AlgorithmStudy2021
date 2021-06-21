from collections import deque
MAX = 1000000000


def findB(A, B):
    queue = deque()
    queue.append((A, 0))
    res = -1

    while len(queue) > 0:
        here, hereCnt = queue.popleft()
        # print(here, hereCnt)

        if here == B:
            res = hereCnt + 1
            break

        cand = [here * 2, here * 10 + 1]
        for there in cand:
            if there <= MAX and there <= B:
                queue.append((there, hereCnt + 1))

    print(res)
    return


if __name__ == '__main__':
    A, B = map(int, input().split())
    findB(A, B)