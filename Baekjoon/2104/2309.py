members = [-1] * 7
isSolved = False


def dfs(here, cnt, rest):
    global members, height, isSolved

    # 이미 답 구했으면 종료
    if isSolved:
        return

    # 아직 답 못구했고, 7명의 키가 100이 되면 답 출력
    if cnt == 7 and rest == 0:
        members.sort(reverse=True)
        for m in members:
            print(height[m])
        isSolved = True
        return

    # 7명인데 100이 아니거나, 9명 전부 지났거나, 이미 100을 넘은 경우 패스
    if cnt >= 7 or here >= 9 or rest <= 0:
        return

    # here번째 난쟁이 포함
    members[cnt] = here
    dfs(here+1, cnt+1, rest-height[here])
    members[cnt] = -1

    # here번째 난쟁이 미포함
    dfs(here+1, cnt, rest)


if __name__ == '__main__':
    height = []
    for _ in range(9):
        height.append(int(input()))
    height.sort(reverse=True)
    dfs(0, 0, 100)