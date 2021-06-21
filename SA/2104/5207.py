def binary_search(num, arr):

    l, r = 0, len(arr)-1
    isExist = False
    isSwitch = True
    direction = 0
    while True:
        mid = (l+r)//2
        m = arr[mid]

        if num == m:
            isExist = True
            break

        if l == r:
            break

        if num < m:
            r = mid - 1
            if isSwitch:
                if direction == 1 or direction == 0:
                    direction = -1
                else:
                    isSwitch = False
                    break
        if num > m:
            l = mid + 1
            if isSwitch:
                if direction == -1 or direction == 0:
                    direction = 1
                else:
                    isSwitch = False
                    break

    return isExist & isSwitch

if __name__ == '__main__':
    TC = int(input())
    for T in range(1, TC + 1):
        N, M = map(int, input().split())
        A = sorted(list(map(int, input().split())))
        B = list(map(int, input().split()))

        cnt = 0
        for x in B:
            if binary_search(x, A):
                cnt += 1

        print("#%d %d" % (T, cnt))