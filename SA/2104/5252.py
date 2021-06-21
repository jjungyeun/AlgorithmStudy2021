N, M = 0, 0
A = []
B = []


def findWord(word):
    global A, N
    skip = False
    for i in range(N):
        if not skip and word[0] == A[i][0]:
            skip = True

        if skip and word[0] != A[i][0]:
            return False

        if word == A[i]:
            return True
    return False


def getCommonWords():
    global A, B
    cnt = 0
    for word in B:
        if findWord(word):
            cnt += 1
    return cnt


if __name__ == '__main__':
    TC = int(input())
    for T in range(1, TC + 1):
        N, M = map(int, input().split())
        A = ['' for _ in range(N)]
        B = ['' for _ in range(M)]
        for i in range(N):
            A[i] = input()
        for i in range(M):
            B[i] = input()

        A.sort()
        res = getCommonWords()
        print("#%d %d" % (T, res))