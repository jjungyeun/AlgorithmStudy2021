import sys


# 배열의 증가 부분 수열의 합 중 최대값을 찾는 함수
def getMaxSum(arr):
    max_sum = 0
    S = [0] * len(arr)  # S[i]: i번째 수를 포함하는 부분증가수열 합의 최댓값

    for i in range(len(arr)):
        # arr[max_j]는 arr[i]보다 작은 수 중 S[j]가 가장 큰 수  (i > j, arr[i] > arr[j])
        # S[i]는 arr[max_j]를 포함하는 부분증가수열에 현재 수 arr[i]를 합한 값
        max_j = i
        for j in range(i):
            if arr[i] > arr[j]:
                if S[max_j] < S[j]:
                    max_j = j
        S[i] = S[max_j] + arr[i]

        max_sum = max(max_sum, S[i])

    return max_sum


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, sys.stdin.readline().split()))

    print(getMaxSum(A))