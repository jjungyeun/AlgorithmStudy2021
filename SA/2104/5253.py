N, M = 0, 0
A, B = [], []


def isPrefix(prefix):
    global A
    for word in A:
        if prefix == word[:len(prefix)]:
            return True
    return False


def getPrefixes():
    global B
    cnt = 0
    for word in B:
        if isPrefix(word):
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

        res = getPrefixes()
        print("#%d %d"%(T, res))