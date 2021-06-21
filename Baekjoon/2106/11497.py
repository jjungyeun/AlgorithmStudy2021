import sys


# 배열의 최소 난이도를 구하는 함수
def getDifficulty(arr):
    # 배열을 내림차순으로 정렬
    arr.sort(reverse=True)
    max_diff = 0

    # 오른쪽 통나무들 높이 차 계속 구하며 최대값과 비교
    idx, prev = 0, arr[0]
    while idx < len(arr):
        crnt = arr[idx]
        max_diff = max(max_diff, abs(prev - crnt))
        prev = crnt
        idx += 2

    # 배열 길이 짝수면 마지막 통나무도 검사 해야함(홀수면 이미 검사 함)
    if len(arr) % 2 == 0:
        idx = len(arr) - 1
    else:
        idx = len(arr) - 2

    # 왼쪽 통나무들 높이 차 계속 구하며 최대값과 비교
    while idx > 0:
        crnt = arr[idx]
        max_diff = max(max_diff, abs(prev-crnt))
        prev = crnt
        idx -= 2

    max_diff = max(max_diff, abs(prev - arr[0]))

    return max_diff


if __name__ == '__main__':
    TC = int(input())
    for T in range(1, TC+1):
        N = int(input())
        L = list(map(int, sys.stdin.readline().split()))

        res = getDifficulty(L)
        print(res)