import sys


# 행렬 mtrx에서 왼쪽 위칸이 (r,c)인 3x3 행렬에 연산을 수행하는 함수
def reverse(mtrx, r, c):
    global H, W
    d = [0, 1, 2]
    for i in range(3):
        for j in range(3):
            hereR, hereC = r + d[i], c + d[j]
            if mtrx[hereR][hereC] == '0':
                mtrx[hereR][hereC] = '1'
            else:
                mtrx[hereR][hereC] = '0'


def getMinOperation():
    global H, W, start, dest
    reverseCnt = 0

    if H >= 3 and W >= 3:
        # 각 위치에 대해 연산을 수행해야하는지, 아닌지를 체크
        for r in range(H-2):
            for c in range(W-2):
                # 왼쪽 상단이 다르면 무조건 뒤집기
                if start[r][c] != dest[r][c]:
                    reverse(start, r, c)
                    reverseCnt += 1

    # 완성된 행렬과 목표행렬이 같으면 연산 횟수 반환, 다르면 -1 반환
    if start == dest:
        return reverseCnt
    else:
        return -1


if __name__ == '__main__':
    H, W = map(int, input().split())
    start, dest = [], []
    for _ in range(H):
        start.append([*sys.stdin.readline().strip()])
    for _ in range(H):
        dest.append([*sys.stdin.readline().strip()])

    print(getMinOperation())