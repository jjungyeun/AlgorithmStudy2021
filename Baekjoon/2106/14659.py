N = int(input())
height_list = list(map(int, input().split()))

longest = 0

start_height, cnt = 0, 0
for i, height in enumerate(height_list):
    if start_height <= height:
        longest = max(longest, cnt)
        start_height = height
        cnt = 0
    else:
        cnt += 1

print(max(longest, cnt))