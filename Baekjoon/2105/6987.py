def nextScore(team1, team2, goal1, goal2, t):
    # 3가지 case
    # 1팀이 더 이겨도 되고, 2팀이 더 져도 되는 경우
    # 두팀 다 더 비겨도 되는 경우
    # 2팀이 더 이겨도 되고, 1팀이 더 져도 되는 경우
    compList = [[0,2], [1,1], [2, 0]]
    dt = [[1,0,0], [0,1,0], [0,0,1]]

    res1 = compList[t][0]
    res2 = compList[t][1]
    if team1[res1] < goal1[res1] and team2[res2] < goal2[res2]:
        return True, [team1[0] + dt[res1][0], team1[1] + dt[res1][1], team1[2] + dt[res1][2]], [team2[0] + dt[res2][0], team2[1] + dt[res2][1], team2[2] + dt[res2][2]]

    return False, [], []


def backTracking(matchNum, currentScore, goalScore):
    global isValid, matchList
    if isValid:
        return
    if matchNum == 15:
        if currentScore == goalScore:
            isValid = True
        return

    team1, team2 = matchList[matchNum]
    crnt1 = currentScore[team1]
    crnt2 = currentScore[team2]
    goal1 = goalScore[team1]
    goal2 = goalScore[team2]

    for t in range(3):
        valid, new1, new2 = nextScore(crnt1, crnt2, goal1, goal2, t)
        if valid:
            newScore = currentScore[:team1] + [new1] + currentScore[team1+1:team2] + [new2] + currentScore[team2+1:]
            # print(newScore)
            backTracking(matchNum + 1, newScore, goalScore)


def baseCase(scoreList):
    sumScore = [0, 0, 0]
    AllWinCnt, drawCnt, AllLoseCnt = 0, 0, 0
    for team in range(6):
        sumTeam = 0
        for i in range(3):
            here = scoreList[team][i]
            sumTeam += here
            sumScore[i] += here
            if i == 0 and here == 5:
                AllWinCnt += 1
            if i == 1 and here > 0:
                drawCnt += 1
            if i == 2 and here == 5:
                AllLoseCnt += 1
        if sumTeam != 5:
            return False

    if sumScore[0] != sumScore[2] or sumScore[1] % 2 != 0:
        return False

    if AllWinCnt > 1 or drawCnt == 1 or AllLoseCnt > 1:
        return False

    return True


if __name__ == '__main__':
    matchList = []
    for i in range(6):
        for j in range(i+1, 6):
            matchList.append((i, j))

    for T in range(4):
        isValid = False
        score = [[0,0,0] for _ in range(6)]
        tmp = list(map(int,input().split()))
        for i in range(len(tmp)):
            score[i//3][i % 3] = tmp[i]

        if baseCase(score):
            score.sort(reverse=True)
            backTracking(0, [[0] * 3 for _ in range(6)], score)
            if isValid:
                print(1, end=' ')
            else:
                print(0, end=' ')
        else:
            print(0, end=' ')







