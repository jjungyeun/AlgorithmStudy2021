import sys


def findMostFamous():
    global N
    res = 0
    for i in range(N):
        one_friends = set()
        two_friends = set()
        for x in adj[i]:
            one_friends.add(x)
        for x in one_friends:
            for y in adj[x]:
                if y != i and y not in one_friends:
                    two_friends.add(y)
        res = max(res, len(one_friends) + len(two_friends))

    print(res)


if __name__ == '__main__':
    N = int(input())
    adj = [[] for _ in range(N)]
    for i in range(N):
        tmp = sys.stdin.readline()
        for j in range(i+1, N):
            if tmp[j] == 'Y':
                adj[i].append(j)
                adj[j].append(i)

    findMostFamous()