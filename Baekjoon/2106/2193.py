N = int(input())

pre, current = 0, 1
for _ in range(N-1):
    pre, current = current, pre + current

print(current)