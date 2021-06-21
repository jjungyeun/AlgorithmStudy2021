def isPrime(n):
    if n % 2 == 0:
        return False
    i = 3
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True


def getInterestingPrimes(N):
    res = []
    if N == 1:
        return [2, 3, 5, 7]

    pre = getInterestingPrimes(N-1)
    for x in pre:
        for i in range(1, 10, 2):
            num = x*10 + i
            if isPrime(num):
                res.append(num)

    return res


if __name__ == '__main__':
    N = int(input())
    res = getInterestingPrimes(N)
    for x in res:
        print(x)