alp2num = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def convert16to2(n):
    if n in alp2num:
        num = alp2num[n]
    else:
        num = int(n)

    res_list = ['','','','']
    for i in range(4):
        res_list[3-i] = str(num%2)
        num = int(num/2)

    res = ''.join(res_list)

    return res


if __name__ == '__main__':
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        N, num16 = input().split(' ')

        num2_list = []
        for i in range(int(N)):
            num2_list.append(convert16to2(num16[i]))

        print("#%d %s" % (test_case, ''.join(num2_list)))
