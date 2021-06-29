def get_longest_list():
    global N, num_list, cnt

    for i in range(N):
        for j in range(i):
            if num_list[j] < num_list[i] and cnt[j] >= cnt[i]:
                cnt[i] = cnt[j] + 1

    return max(cnt)


if __name__ == '__main__':
    N = int(input())
    num_list = list(map(int, input().split()))
    cnt = [1 for _ in range(N)]
    print(get_longest_list())