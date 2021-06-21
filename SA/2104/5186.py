
def convert10to2(n):
    res = ''
    num = n
    while True:
        num = num*2
        if num >= 1.0:
            res += '1'
            if num == 1.0:
                break
            num = num - 1.0
        else:
            res += '0'

        if len(res) > 12:
            return 'overflow'

    return res


if __name__ == '__main__':
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        N = float(input())
        res = convert10to2(N)

        print("#%d %s" % (test_case, res))
