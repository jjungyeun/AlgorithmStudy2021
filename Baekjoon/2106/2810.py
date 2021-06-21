N = int(input())
seat = input().strip()
numS, numL = 0, 0

for s in seat:
    if s == 'S':
        numS += 1
    else:
        numL += 1

holder = numS + numL // 2 + 1

if holder < N:
    print(holder)
else:
    print(N)