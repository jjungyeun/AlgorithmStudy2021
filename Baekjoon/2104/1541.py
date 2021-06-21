def getMinResult(exp):
    num = ''
    isMinus = False
    res = 0
    for s in exp:
        # '-' 나오기 이전까지는 모두 더하기
        if not isMinus:
            if s == '-':
                isMinus = True
            if s == '+' or s == '-':
                res += int(num)
                num = ''
            else:
                num += s
        # '-' 한번이라도 나오고 나면 모두 빼기
        else:
            if s == '+' or s == '-':
                res -= int(num)
                num = ''
            else:
                num += s
    if isMinus:
        res -= int(num)
    else:
        res += int(num)

    print(res)


if __name__ == '__main__':
    getMinResult(input())
