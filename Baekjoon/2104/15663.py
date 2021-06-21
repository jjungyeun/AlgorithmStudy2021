restCnt = [0] * 8
idx2num, num2idx = dict(), dict()


# 결과 배열 출력 함수
def printArr(arr):
    for x in arr:
        print(x, end=' ')
    print()


# depth번째 숫자 선택 함수
# 선택횟수가 남은(restCnt[i] > 0) 숫자 선택
def backTracking(depth, M, arr):
    global restCnt, idx2num
    if depth == M:
        printArr(arr)
        return

    n = len(idx2num)
    for i in range(n):
        if restCnt[i] > 0:
            restCnt[i] -= 1
            backTracking(depth+1, M, arr + [idx2num[i]])
            restCnt[i] += 1
    return


if __name__ == '__main__':
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    num_set = sorted(set(nums))
    for i in range(len(num_set)):
        idx2num[i] = num_set[i]
        num2idx[num_set[i]] = i
    for x in nums:
        restCnt[num2idx[x]] += 1

    backTracking(0, M, [])