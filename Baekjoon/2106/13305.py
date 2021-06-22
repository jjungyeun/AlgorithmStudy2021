import sys

def get_min_pay():
    global N, price, dist

    total_cost = 0
    minist = price[0]
    for idx, p in enumerate(price[:-1]):
        minist = min(minist, p)
        total_cost += minist * dist[idx]
    return total_cost


if __name__ == '__main__':
    N = int(input())
    dist = list(map(int, sys.stdin.readline().split()))
    price = list(map(int, sys.stdin.readline().split()))

    print(get_min_pay())