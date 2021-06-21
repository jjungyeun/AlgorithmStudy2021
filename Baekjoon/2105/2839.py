def getMinimumBag(W):
    if W >= 5:
        bag5 = W // 5
        bag3 = 0
        for i in range(bag5, -1, -1):
            res = W - i * 5
            if res % 3 == 0:
                bag3 = res // 3
                print(i + bag3)
                return
            bag3 += 1
    else:
        if W == 3:
            print(1)
            return
    print(-1)
    return


if __name__ == '__main__':
    N = int(input())
    getMinimumBag(N)