def countNum(card_list):
    cnt_list = [0 for i in range(0, 10)]
    for card in card_list:
        cnt_list[card] += 1
    return cnt_list


def isRun(card_list):
    cnt_list = countNum(card_list)
    for i in range(0,8):
        if cnt_list[i] > 0 and cnt_list[i+1] > 0 and cnt_list[i+2] > 0:
            return True
    return False


def isTriplet(card_list):
    cnt_list = countNum(card_list)
    for cnt in cnt_list:
        if cnt >= 3:
            return True
    return False


def canWin(card_list):
    return isRun(card_list) or isTriplet(card_list)


def whoIsWinner(player1, player2):
    for turn in range(3, 7):
        list1 = player1[:turn]
        list2 = player2[:turn]
        if canWin(list1):
            return 1
        if canWin(list2):
            return 2

    return 0


if __name__ == '__main__':
    TC = int(input())
    for T in range(1, TC + 1):
        tmp = input().split(' ')
        player1 = [int(tmp[2*i]) for i in range(0,6)]
        player2 = [int(tmp[2*i+1]) for i in range(0,6)]

        res = whoIsWinner(player1, player2)
        print("#%d %d" % (T, res))