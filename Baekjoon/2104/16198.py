# bound = (현재까지의 에너지) + (앞으로 제거할 개수로 나올 수 있는 최대 곱)
def getBound(energy, weights):
    nums = sorted(weights, reverse=True)
    bound = energy
    for i in range(1, len(weights)-1):
        bound += (nums[0] * nums[i])

    return bound


def backTracking(depth, energy, weights):
    global N, W, MAX

    # 구슬 2개 남으면 종료
    if depth == N-2:
        MAX = max(MAX, energy)
        return

    # 유망하지 않으면 return
    if depth != 0 and getBound(energy, weights) < MAX:
        return

    for i in range(1, len(weights)-1):
        backTracking(depth+1, energy + weights[i-1] * weights[i+1], weights[:i] + weights[i+1:])


if __name__ == '__main__':
    N = int(input())
    W = list(map(int, input().split()))
    MAX = 0
    backTracking(0, 0, W)
    print(MAX)
