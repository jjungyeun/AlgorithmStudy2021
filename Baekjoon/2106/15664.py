N, M = map(int, input().split())
num_list, num_cnt, selected = [], [], []

pre = None
for num in sorted(list(map(int, input().split()))):
    if pre is None or pre != num:
        num_list.append(num)
        num_cnt.append(1)
    else:
        num_cnt[-1] += 1
    pre = num


def dfs(depth):
    # M개 선택되면 출력
    if len(selected) == M:
        for n in selected:
            print(n, end=' ')
        print()
        return

    # M개 선택 안했는데 숫자 남은거 없으면 종료
    if depth >= len(num_list):
        return

    # 이번 숫자 선택
    if num_cnt[depth] > 0:
        num_cnt[depth] -= 1
        selected.append(num_list[depth])
        dfs(depth)
        num_cnt[depth] += 1
        selected.pop()

    # 이번 숫자 선택 X
    dfs(depth+1)

dfs(0)